import unittest

from ingest.parse_faa_sightings import construire_evenement, extraire_champs


class IngestionTests(unittest.TestCase):
    def test_evasif_reste_inconnu_sans_information(self):
        self.assertIsNone(extraire_champs("UAS sighting with no maneuver detail")["evasif"])

    def test_evasif_distingue_oui_et_non(self):
        self.assertIs(extraire_champs("NO EVASIVE ACTION TAKEN")["evasif"], False)
        self.assertIs(extraire_champs("EVASIVE ACTION WAS TAKEN")["evasif"], True)

    def test_evenement_faa_est_explicitement_externe(self):
        evenement = construire_evenement(
            "2026-07-01", "TX", "Dallas", "PRELIM INFO FROM FAA OPS/UAS SIGHTING/ AT /1200C/"
        )

        self.assertEqual(evenement["source_type"], "test_faa_import")
        self.assertEqual(evenement["statut_preuve"], "externe")
        self.assertEqual(evenement["nature"], "a_verifier")
        self.assertIsNone(evenement["latitude"])
        self.assertIsNone(evenement["longitude"])


if __name__ == "__main__":
    unittest.main()
