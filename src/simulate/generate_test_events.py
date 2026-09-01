"""
VIGIE — Generateur d'evenements simules

Objectif : tester classification (src/classification/classifier.py) et
correlation (src/correlation/correlation_engine.py) BOUT EN BOUT sans
attendre le capteur RF physique ni la configuration Supabase.

Ecrit un fichier JSON local (evenements_simules.json) -- ne touche
jamais la vraie base de production. A lancer avec :
  python src/simulate/generate_test_events.py
"""

import argparse
import json
import random
from datetime import datetime, timedelta

# Zone de reference : aeroport de Lome (coordonnees approximatives)
LAT_BASE, LON_BASE = 6.1656, 1.2545

EXEMPLES_AGENT = [
    ("Bagage abandonne signale", "Un bagage sans proprietaire identifie pres du point de controle 2"),
    ("Comportement suspect", "Un individu observe a plusieurs reprises pres de la cloture perimetrique"),
    ("Acces badge irregulier", "Tentative d'acces avec un badge expire au poste de controle nord"),
]

EXEMPLES_RF = [
    ("Signature RF drone detectee", "Frequence: 2437 MHz, force: -42 dB, hors zone autorisee"),
    ("Signature RF drone detectee", "Frequence: 5805 MHz, force: -55 dB, direction sud-ouest"),
    ("Signal RF ambigu", "Frequence: 2450 MHz, force: -70 dB, signature non concluante"),
]

def generer_evenement(i, horodatage_base, rng):
    est_rf = rng.random() < 0.5
    titre, desc = rng.choice(EXEMPLES_RF if est_rf else EXEMPLES_AGENT)
    return {
        "id": i,
        "source_type": "rf_drone" if est_rf else "agent_terrain",
        "source_id": "rf_capteur_01" if est_rf else "agent_0" + str(rng.randint(1, 3)),
        "titre": titre,
        "description": desc,
        "latitude": LAT_BASE + rng.uniform(-0.03, 0.03),
        "longitude": LON_BASE + rng.uniform(-0.03, 0.03),
        "horodatage": (horodatage_base + timedelta(minutes=rng.randint(0, 480))).isoformat(),
        "nature": "a_verifier",
        "criticite": 20,
        "justification": "Événement simulé pour tester le parcours VIGIE",
        "statut": "nouveau",
        "statut_preuve": "simule",
    }

def generer_lot(n=12, seed=2026):
    base = datetime(2026, 8, 16, 18, 0, 0)
    rng = random.Random(seed)
    return [generer_evenement(i, base, rng) for i in range(1, n + 1)]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Génère des événements simulés reproductibles")
    parser.add_argument("--count", type=int, default=12, help="nombre d'événements")
    parser.add_argument("--seed", type=int, default=2026, help="graine aléatoire")
    parser.add_argument("--output", default="evenements_simules.json", help="fichier JSON de sortie")
    args = parser.parse_args()
    if args.count < 1:
        parser.error("--count doit être supérieur à zéro")

    evenements = generer_lot(args.count, args.seed)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(evenements, f, ensure_ascii=False, indent=2)
    print(str(len(evenements)) + " evenements simules ecrits dans " + args.output)
    print("Pour tester la correlation dessus :")
    print(
        "  PYTHONPATH=src python -c \"import json; "
        "from correlation.correlation_engine import chercher_correlations; "
        f"evts=json.load(open('{args.output}', encoding='utf-8')); "
        "[print(l) for l in chercher_correlations(evts)]\""
    )
