"""
VIGIE — Ingestion FAA UAS Sightings (test Niveau 1 : schema + ingestion)

Objectif : valider que le pipeline VIGIE peut transformer un signalement
en texte libre/semi-structure en evenement conforme au schema commun
(`evenements`). PAS une source de donnees togolaises -- usage explicite
et limite au test technique de l'extraction, comme documente dans
docs/donnees.md (Niveau 1 du plan de test en 4 niveaux).

Format source : fichiers .xlsx publies par la FAA
(faa.gov/uas/resources/public_records/uas_sightings_report), colonnes
reellement remplies : Date, State, City, Summary. Le champ Summary est
un texte libre avec heure, altitude, distance/direction par rapport a
un aeroport, et notification eventuelle des forces de l'ordre.

IMPORTANT : aucune latitude/longitude n'est deduite ici. Le point de
vigilance deja documente (docs/materiel.md, notes de recherche) est
clair : ne jamais traiter une distance/direction textuelle comme une
mesure geodesique precise. Le geocodage reste une etape separee et
controlee, non faite par ce script.
"""

import re
import json
from datetime import datetime

RE_TYPE_RAPPORT = re.compile(r"^(PRELIM|CLOSE-OUT) INFO FROM FAA OPS")
RE_TYPE_EVENEMENT = re.compile(r"/UAS (SIGHTING|INCIDENT)/")
RE_HEURE = re.compile(r"/(\d{4})([CEMPA])/")  # heure locale + fuseau (C/E/M/P/A)
RE_ALTITUDE = re.compile(r"WHILE \w+ BOUND AT ([\d,]+) FEET")
RE_DISTANCE_AEROPORT = re.compile(r"(\d+(?:\.\d+)?)\s+([NSEW]{1,3})\s+([A-Z]{3,4})\.")
RE_EVASIF_NON = re.compile(r"NO EVASIVE ACTION TAKEN", re.IGNORECASE)
RE_EVASIF_OUI = re.compile(r"(?<!NO )EVASIVE ACTION(?: WAS)? TAKEN", re.IGNORECASE)

FUSEAUX = {"E": "America/New_York", "C": "America/Chicago",
           "M": "America/Denver", "P": "America/Los_Angeles", "A": "America/Anchorage"}


def extraire_champs(summary):
    """Extrait les champs structures d'un texte Summary FAA.
    Retourne un dict ; les champs non trouves restent None -- ne
    jamais deviner une valeur absente."""
    champs = {
        "type_rapport": None, "nature": None, "heure_locale": None,
        "fuseau": None, "altitude_pieds": None, "distance_nm": None,
        "direction": None, "code_aeroport": None, "evasif": None,
    }

    m = RE_TYPE_RAPPORT.search(summary)
    if m:
        champs["type_rapport"] = m.group(1)

    m = RE_TYPE_EVENEMENT.search(summary)
    if m:
        champs["nature"] = m.group(1)

    m = RE_HEURE.search(summary)
    if m:
        champs["heure_locale"] = m.group(1)
        champs["fuseau"] = m.group(2)

    m = RE_ALTITUDE.search(summary)
    if m:
        champs["altitude_pieds"] = int(m.group(1).replace(",", ""))

    m = RE_DISTANCE_AEROPORT.search(summary)
    if m:
        champs["distance_nm"] = float(m.group(1))
        champs["direction"] = m.group(2)
        champs["code_aeroport"] = m.group(3)

    if RE_EVASIF_NON.search(summary):
        champs["evasif"] = False
    elif RE_EVASIF_OUI.search(summary):
        champs["evasif"] = True

    return champs


def construire_evenement(row_date, state, city, summary):
    """Construit un evenement conforme au schema commun `evenements`.
    source_type = 'test_faa_import' -- distinct de 'agent_terrain' et
    'rf_drone' pour ne jamais confondre ce jeu de test americain avec
    une vraie source togolaise (point de vigilance deja documente)."""
    champs = extraire_champs(str(summary))

    horodatage = row_date
    if hasattr(row_date, "isoformat"):
        horodatage = row_date.isoformat()

    return {
        "source_type": "test_faa_import",
        "source_id": "faa_uas_sightings_fy26_q3",
        "titre": "Signalement UAS -- " + str(city) + ", " + str(state),
        "description": json.dumps(champs, ensure_ascii=False),
        "latitude": None,   # geocodage volontairement non fait ici
        "longitude": None,
        "horodatage": horodatage,
        "nature": "a_verifier",
        "criticite": 20,
        "justification": "Donnée externe à examiner ; aucune conclusion opérationnelle",
        "statut": "a_verifier",
        "statut_preuve": "externe",
    }


def parser_fichier(chemin_xlsx):
    """Lit le fichier FAA et retourne une liste d'evenements VIGIE.
    Necessite pandas + openpyxl (deja utilises ailleurs dans le projet)."""
    import pandas as pd
    df = pd.read_excel(chemin_xlsx, usecols=["Date", "State", "City", "Summary"])
    evenements = []
    for _, row in df.iterrows():
        evenements.append(construire_evenement(row["Date"], row["State"], row["City"], row["Summary"]))
    return evenements


if __name__ == "__main__":
    import sys
    chemin = sys.argv[1] if len(sys.argv) > 1 else "FY26_Q3_UAS_Sightings.xlsx"
    evenements = parser_fichier(chemin)
    print(str(len(evenements)) + " evenement(s) extrait(s)")
    print("\nExemple (premier evenement) :")
    print(json.dumps(evenements[0], ensure_ascii=False, indent=2))

    # Statistiques rapides pour verifier la qualite d'extraction
    n_altitude = sum(1 for e in evenements if json.loads(e["description"])["altitude_pieds"] is not None)
    n_distance = sum(1 for e in evenements if json.loads(e["description"])["distance_nm"] is not None)
    print("\nChamp altitude extrait : " + str(n_altitude) + "/" + str(len(evenements)))
    print("Champ distance/aeroport extrait : " + str(n_distance) + "/" + str(len(evenements)))
