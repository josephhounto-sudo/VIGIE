import json
import unittest
from unittest.mock import patch

import classification.classifier as module


class ClassificationTests(unittest.TestCase):
    def test_extraire_json_borne_la_criticite(self):
        nature, criticite, raison = module.extraire_json(
            json.dumps({"nature": "anomalie", "criticite": 180, "raison": "Signal incomplet"})
        )

        self.assertEqual(nature, "anomalie")
        self.assertEqual(criticite, 100)
        self.assertEqual(raison, "Signal incomplet")

    def test_un_modele_ne_peut_pas_confirmer_seul(self):
        nature, criticite, _ = module.extraire_json(
            json.dumps({"nature": "incident_confirme", "criticite": 95, "raison": "Texte affirmatif"})
        )

        self.assertEqual(nature, "a_verifier")
        self.assertEqual(criticite, 30)

    def test_repli_sans_cle_api(self):
        with patch.object(module, "GROQ_API_KEY", ""), patch.object(module, "GEMINI_API_KEY", ""):
            nature, criticite, raison, source = module.classifier(
                {"source_type": "agent_terrain", "titre": "Observation", "description": "À examiner"}
            )

        self.assertEqual((nature, criticite, source), ("a_verifier", 20, "repli"))
        self.assertIn("IA indisponible", raison)


if __name__ == "__main__":
    unittest.main()
