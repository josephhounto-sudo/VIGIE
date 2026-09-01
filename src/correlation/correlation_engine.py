"""
VIGIE — Volet LOGICIEL — Moteur de correlation (implementation reelle)

Choix assume : correlation DETERMINISTE (distance geographique +
ecart de temps), PAS d'appel IA. Rapprocher deux points GPS et deux
horodatages est un calcul exact -- y mettre un LLM serait plus lent,
plus cher, et moins auditable qu'une formule. L'IA de VIGIE est
reservee a la classification (nature/criticite), qui EST un
jugement -- pas a la geometrie, qui n'en est pas un.

Meme seuil strict que moteur_connexions.py (Sentinelle) : un lien
n'est cree que si le score depasse un seuil, pour eviter les faux
rapprochements.
"""

import math
from datetime import datetime, timezone

RAYON_KM = 2.0          # distance max pour considerer "meme zone"
FENETRE_HEURES = 6.0    # ecart de temps max pour considerer "meme creneau"
SEUIL_SCORE_LIEN = 60   # meme convention que Sentinelle (score_lien >= 60)
MAX_LIENS_PAR_EVENEMENT = 5


def _coordonnees_valides(lat, lon):
    valeurs = (lat, lon)
    sont_finies = all(isinstance(v, (int, float)) and math.isfinite(v) for v in valeurs)
    return sont_finies and -90 <= lat <= 90 and -180 <= lon <= 180

def distance_km(lat1, lon1, lat2, lon2):
    """Formule de haversine -- distance a vol d'oiseau entre 2 points GPS."""
    if not _coordonnees_valides(lat1, lon1) or not _coordonnees_valides(lat2, lon2):
        return None
    R = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp = math.radians(lat2 - lat1)
    dl = math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def ecart_heures(t1, t2):
    """t1, t2 : chaines ISO ou objets datetime."""
    if isinstance(t1, str):
        t1 = datetime.fromisoformat(t1)
    if isinstance(t2, str):
        t2 = datetime.fromisoformat(t2)
    if t1.tzinfo is None:
        t1 = t1.replace(tzinfo=timezone.utc)
    else:
        t1 = t1.astimezone(timezone.utc)
    if t2.tzinfo is None:
        t2 = t2.replace(tzinfo=timezone.utc)
    else:
        t2 = t2.astimezone(timezone.utc)
    return abs((t1 - t2).total_seconds()) / 3600.0

def evaluer_lien(evt_a, evt_b):
    """Retourne (score_lien, type_lien, raison) ou None si aucun lien
    ne depasse le seuil. Score decroit lineairement avec la distance
    et l'ecart de temps -- plus proche en espace ET en temps = score
    plus eleve."""
    dist = distance_km(evt_a.get("latitude"), evt_a.get("longitude"),
                        evt_b.get("latitude"), evt_b.get("longitude"))
    ecart = None
    if evt_a.get("horodatage") and evt_b.get("horodatage"):
        try:
            ecart = ecart_heures(evt_a["horodatage"], evt_b["horodatage"])
        except Exception:
            ecart = None

    if dist is None or ecart is None:
        return None
    if dist > RAYON_KM or ecart > FENETRE_HEURES:
        return None

    score_distance = max(0, 100 * (1 - dist / RAYON_KM))
    score_temps = max(0, 100 * (1 - ecart / FENETRE_HEURES))
    score = round((score_distance + score_temps) / 2)

    if score < SEUIL_SCORE_LIEN:
        return None

    if dist < 0.3 and ecart < 1:
        type_lien = "proximite_forte"
        raison = "Proximite forte de lieu et de temps -- relation a verifier"
    elif dist < RAYON_KM:
        type_lien = "meme_zone"
        raison = "Evenements dans un rayon de " + str(round(dist, 2)) + " km"
    return score, type_lien, raison

def chercher_correlations(evenements_recents, max_liens_par_evenement=MAX_LIENS_PAR_EVENEMENT):
    """Compare chaque paire d'evenements recents (liste de dicts avec
    id, latitude, longitude, horodatage). Retourne la liste des liens
    a creer. Le prototype exige deux source_type distincts et borne le
    nombre de liens par evenement. A brancher sur une base securisee ;
    ici la fonction reste pure et testable hors-ligne."""
    liens = []
    n = len(evenements_recents)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = evenements_recents[i], evenements_recents[j]
            if a.get("id") is None or b.get("id") is None:
                continue
            if a.get("id") == b.get("id"):
                continue
            source_a = a.get("source_type")
            source_b = b.get("source_type")
            if not source_a or not source_b or source_a == source_b:
                continue
            resultat = evaluer_lien(a, b)
            if resultat:
                score, type_lien, raison = resultat
                liens.append({
                    "evenement_a_id": a.get("id"),
                    "evenement_b_id": b.get("id"),
                    "score_lien": score,
                    "type_lien": type_lien,
                    "raison": raison,
                })
    liens.sort(key=lambda lien: lien["score_lien"], reverse=True)
    comptes = {}
    retenus = []
    for lien in liens:
        a_id = lien["evenement_a_id"]
        b_id = lien["evenement_b_id"]
        if comptes.get(a_id, 0) >= max_liens_par_evenement:
            continue
        if comptes.get(b_id, 0) >= max_liens_par_evenement:
            continue
        retenus.append(lien)
        comptes[a_id] = comptes.get(a_id, 0) + 1
        comptes[b_id] = comptes.get(b_id, 0) + 1
    return retenus

if __name__ == "__main__":
    exemples = [
        {"id": 1, "source_type": "rf_drone", "latitude": 6.1319, "longitude": 1.2228,
         "horodatage": "2026-08-16T20:00:00"},
        {"id": 2, "source_type": "agent_terrain", "latitude": 6.1330, "longitude": 1.2235,
         "horodatage": "2026-08-16T20:40:00"},
        {"id": 3, "source_type": "remote_id", "latitude": 6.5000, "longitude": 1.5000,
         "horodatage": "2026-08-17T09:00:00"},
    ]
    for lien in chercher_correlations(exemples):
        print(lien)
