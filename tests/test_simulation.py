import unittest

from simulate.generate_test_events import generer_lot


class SimulationTests(unittest.TestCase):
    def test_simulation_reproductible(self):
        self.assertEqual(generer_lot(10, seed=42), generer_lot(10, seed=42))
        self.assertNotEqual(generer_lot(10, seed=42), generer_lot(10, seed=43))

    def test_simulation_annonce_sa_provenance(self):
        evenements = generer_lot(5, seed=2026)

        self.assertTrue(all(evt["statut_preuve"] == "simule" for evt in evenements))
        self.assertTrue(all(evt["nature"] == "a_verifier" for evt in evenements))
        self.assertTrue(all(evt["criticite"] == 20 for evt in evenements))


if __name__ == "__main__":
    unittest.main()
