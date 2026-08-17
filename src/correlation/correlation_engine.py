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
from datetime import datetime

RAYON_KM = 2.0          # distance max pour considerer "meme zone"
FENETRE_HEURES = 6.0    # ecart de temps max pour considerer "meme creneau"
SEUIL_SCORE_LIEN = 60   # meme convention que Sentinelle (score_lien >= 60)

def distance_km(lat1, lon1, lat2, lon2):
    """Formule de haversine -- distance a vol d'oiseau entre 2 points GPS."""
    if None in (lat1, lon1, lat2, lon2):
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
        type_lien = "recurrence"
        raison = "Meme zone rapprochee et meme creneau -- forte probabilite de lien reel"
    elif dist < RAYON_KM:
        type_lien = "meme_zone"
        raison = "Evenements dans un rayon de " + str(round(dist, 2)) + " km"
    else:
        type_lien = "meme_creneau"
        raison = "Evenements a " + str(round(ecart, 1)) + "h d'ecart"

    return score, type_lien, raison

def chercher_correlations(evenements_recents):
    """Compare chaque paire d'evenements recents (liste de dicts avec
    id, latitude, longitude, horodatage). Retourne la liste des liens
    a creer. A brancher sur une vraie requete Supabase une fois les
    cles configurees -- ici la fonction est pure, testable hors-ligne."""
    liens = []
    n = len(evenements_recents)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = evenements_recents[i], evenements_recents[j]
            if a.get("id") == b.get("id"):
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
    return liens

if __name__ == "__main__":
    exemples = [
        {"id": 1, "latitude": 6.1319, "longitude": 1.2228, "horodatage": "2026-08-16T20:00:00"},
        {"id": 2, "latitude": 6.1330, "longitude": 1.2235, "horodatage": "2026-08-16T20:40:00"},
        {"id": 3, "latitude": 6.5000, "longitude": 1.5000, "horodatage": "2026-08-17T09:00:00"},
    ]
    for lien in chercher_correlations(exemples):
        print(lien)
