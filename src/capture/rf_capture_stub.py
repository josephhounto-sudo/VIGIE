"""
VIGIE — Volet MATERIEL — Capture RF (squelette)

Objectif : ecouter le spectre 2.4/5.8 GHz via un dongle RTL-SDR,
detecter une signature de drone, et ecrire un evenement conforme
au schema commun (schema/migration.sql, table `evenements`).

Ce fichier est un SQUELETTE, pas du code fonctionnel -- chaque
TODO correspond a une decision qui depend du materiel reellement
en main (modele exact du dongle, antenne, distance de test).

Stack recommandee (a verifier a l'achat du materiel) :
- rtl-sdr (pilote bas niveau, projet osmocom/rtl-sdr sur GitHub)
- SoapySDR ou pyrtlsdr pour l'acces Python
- numpy / scipy pour la FFT -> spectrogramme
- classification : d'abord un seuil simple sur l'energie dans les
  bandes connues (2.4/5.8 GHz), un modele ML n'est utile qu'une
  fois des donnees reelles collectees sur le terrain.
"""

import json
from datetime import datetime

# ─── CONTRAT DE SORTIE (ne pas devier de cette forme) ─────────
# Doit correspondre exactement aux colonnes de `evenements` dans
# schema/migration.sql. Le volet logiciel consomme cette forme,
# qu'elle vienne d'un vrai capteur ou d'un evenement simule.

def construire_evenement(detecte, frequence_mhz, force_signal_db, lat=None, lon=None):
    """Construit un dict pret a inserer dans la table `evenements`.
    TODO : remplacer la detection par la vraie lecture SDR une fois
    le materiel recu (RTL-SDR + antenne)."""
    return {
        "source_type": "rf_drone",
        "source_id": "rf_capteur_01",  # TODO : identifiant reel si plusieurs capteurs
        "titre": "Signature RF drone detectee" if detecte else "Rien a signaler",
        "description": (
            "Frequence: " + str(frequence_mhz) + " MHz, "
            "force: " + str(force_signal_db) + " dB"
        ),
        "latitude": lat,   # TODO : position fixe du capteur, ou None si non geolocalise
        "longitude": lon,
        "horodatage": datetime.now().isoformat(),
        "statut": "nouveau",
    }

def scanner_spectre():
    """TODO -- coeur du volet materiel.
    1. Ouvrir le flux SDR (pyrtlsdr ou SoapySDR).
    2. Faire une FFT glissante sur les bandes 2.4 GHz et 5.8 GHz.
    3. Comparer l'energie detectee a une signature connue (motif
       de saut de frequence, largeur de bande caracteristique).
    4. Si le seuil est depasse, appeler construire_evenement(True, ...).
    Ne PAS implementer de bout en bout avant d'avoir le dongle en
    main -- tester d'abord sur un enregistrement IQ de reference
    (des jeux d'exemples existent sur des depots publics de
    detection RF de drones, a chercher/verifier au moment venu)."""
    raise NotImplementedError("A implementer une fois le RTL-SDR recu")

def envoyer_vers_supabase(evenement):
    """TODO -- reutiliser le pattern exact de inserer() dans
    collecteurs/collecteur_rss.py (Sentinelle) : meme client
    supabase-py, meme gestion d'erreur best-effort."""
    print("[STUB] evenement pret a inserer :", json.dumps(evenement, ensure_ascii=False))

if __name__ == "__main__":
    # Exemple de test SANS materiel : simule un evenement pour
    # valider que le format est bien conforme au schema commun.
    exemple = construire_evenement(detecte=True, frequence_mhz=2437, force_signal_db=-45)
    envoyer_vers_supabase(exemple)
