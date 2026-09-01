import unittest
from collections import Counter

from correlation.correlation_engine import ecart_heures, evaluer_lien, chercher_correlations


def evenement(identifiant, source, latitude=6.1656, longitude=1.2545, heure="2026-08-16T20:00:00Z"):
    return {
        "id": identifiant,
        "source_type": source,
        "latitude": latitude,
        "longitude": longitude,
        "horodatage": heure,
    }


class CorrelationTests(unittest.TestCase):
    def test_proximite_forte_reste_une_hypothese(self):
        resultat = evaluer_lien(
            evenement(1, "agent_terrain"),
            evenement(2, "remote_id", latitude=6.166, heure="2026-08-16T20:20:00Z"),
        )

        self.assertIsNotNone(resultat)
        score, type_lien, raison = resultat
        self.assertGreaterEqual(score, 60)
        self.assertEqual(type_lien, "proximite_forte")
        self.assertIn("verifier", raison)

    def test_coordonnees_invalides_refusees(self):
        resultat = evaluer_lien(evenement(1, "agent_terrain", latitude=999), evenement(2, "remote_id"))
        self.assertIsNone(resultat)

    def test_dates_naive_et_utc_sont_comparables(self):
        self.assertEqual(ecart_heures("2026-08-16T20:00:00", "2026-08-16T20:00:00+00:00"), 0)

    def test_recherche_exige_deux_sources_et_borne_le_bruit(self):
        evenements = [
            evenement(i, "agent_terrain" if i % 2 else "remote_id", heure=f"2026-08-16T20:{i:02d}:00Z")
            for i in range(1, 12)
        ]
        liens = chercher_correlations(evenements, max_liens_par_evenement=2)
        comptes = Counter(
            identifiant
            for lien in liens
            for identifiant in (lien["evenement_a_id"], lien["evenement_b_id"])
        )

        self.assertTrue(liens)
        self.assertLessEqual(max(comptes.values()), 2)
        for lien in liens:
            a = next(evt for evt in evenements if evt["id"] == lien["evenement_a_id"])
            b = next(evt for evt in evenements if evt["id"] == lien["evenement_b_id"])
            self.assertNotEqual(a["source_type"], b["source_type"])

    def test_recherche_ignore_une_source_non_identifiee(self):
        evenements = [
            evenement(1, None),
            evenement(2, "agent_terrain", latitude=6.166, heure="2026-08-16T20:05:00Z"),
        ]

        self.assertEqual(chercher_correlations(evenements), [])


if __name__ == "__main__":
    unittest.main()
