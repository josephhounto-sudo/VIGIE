import csv
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def lire_csv(nom):
    with (ROOT / "data" / nom).open(encoding="utf-8", newline="") as fichier:
        return list(csv.DictReader(fichier))


class DataQualityTests(unittest.TestCase):
    def test_referentiel_aeroports_unique_et_borne(self):
        aeroports = lire_csv("togo_airports.csv")
        identifiants = [ligne["ident"] for ligne in aeroports]

        self.assertEqual(len(aeroports), 7)
        self.assertEqual(len(identifiants), len(set(identifiants)))
        self.assertTrue(all(-90 <= float(ligne["latitude_deg"]) <= 90 for ligne in aeroports))
        self.assertTrue(all(-180 <= float(ligne["longitude_deg"]) <= 180 for ligne in aeroports))

    def test_frequences_renseignees_dans_la_bande_civile(self):
        frequences = lire_csv("togo_airport_frequencies.csv")

        for ligne in frequences:
            valeur = ligne["frequency_mhz"].strip()
            if valeur:
                self.assertTrue(108 <= float(valeur) <= 137)

    def test_schema_refuse_les_droits_anonymes_complets(self):
        schema = (ROOT / "schema" / "migration.sql").read_text(encoding="utf-8").lower()

        self.assertNotIn("grant all on public.evenements to anon", schema)
        self.assertIn("revoke all on public.evenements from anon", schema)


if __name__ == "__main__":
    unittest.main()
