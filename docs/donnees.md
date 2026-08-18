# Bases de données — état consolidé

> Consolide les recherches précédentes (Manus + vérifications Claude,
> 17-18/08/2026). Remplace la lecture éparpillée des PDF de recherche —
> ce document est la référence à jour.

## Chargé et disponible dans le repo

| Source | Emplacement | Statut |
|---|---|---|
| Aéroports du Togo (OurAirports) | `data/togo_airports.csv` + fichiers associés | ✅ Chargé le 18/08/2026, 7 aéroports, cohérent avec les coordonnées déjà utilisées dans le dashboard |
| FAA UAS Sightings (test ingestion) | `src/ingest/parse_faa_sightings.py` | ✅ Parseur testé, 600 événements extraits, 90%/76% de taux d'extraction |

## Vérifié, décision prise, pas chargé dans le repo

### RFUAV — licence confirmée, taille rédhibitoire pour le brut

- Licence Apache-2.0 confirmée (fiche Hugging Face du dataset).
- Le jeu de données brut complet fait environ 1,3 To — incompatible
  avec un contexte mobile-first, budget serré, connectivité togolaise.
- **Décision : ne pas télécharger le jeu brut.** Deux alternatives
  légères existent, mentionnées par les auteurs eux-mêmes :
  - Un sous-ensemble curé pour la détection, hébergé sur Roboflow.
  - Des poids de modèle déjà entraînés, publiés sur Hugging Face —
    évaluer un modèle existant est plus rapide et plus réaliste que
    ré-entraîner depuis les données brutes.
- Prochaine étape si la Couche 2 avance : évaluer les poids
  Hugging Face directement, avant d'envisager le sous-ensemble
  Roboflow.

### GéoData Togo — catalogue confirmé, présence de DXXX non encore vérifiée

Le portail `geodata.gouv.tg` héberge un catalogue confirmé de 177 jeux
publics, dont une famille "Aéroports" complète (Établissements,
Bâtiments, Cuves, Énergies, Pistes, Véhicules), source PRISE
2021/2022, téléchargeable en CSV/XLSX/KML/GEOJSON/SHP. Le
téléchargement direct de la fiche "Aéroports - Établissements" n'a pas
encore produit de fichier exploitable lors du test — la présence
effective de Lomé (DXXX) reste à confirmer en re-testant le
téléchargement ou en contactant le portail. Accès en principe gratuit
et sans compte, réutilisation potentiellement soumise à une demande
(jusqu'à 20 jours ouvrables).

### OSM Togo (Geofabrik) — bloqué techniquement, pas conceptuellement

Le téléchargement direct n'est pas accessible depuis l'environnement
d'exécution de Claude (domaine hors liste autorisée). Pas un problème
de fond — juste une limite d'outil. Deux options pour Joe : télécharger
manuellement et uploader dans une session future, ou s'en passer pour
le MVP (`togo_airports.csv` suffit largement pour la démonstration).
Non bloquant pour le 31 août.

### DroneRF, UAVSig

Toujours non vérifiés directement (pages protégées par anti-robot lors
des recherches précédentes). Pas prioritaires — RFUAV (via Hugging
Face) couvre déjà le besoin de validation de laboratoire pour la
Couche 2.

## Rappel — ce qui n'existe pas

Aucune base africaine ouverte ne réunit Remote ID, RF drone et
signalements de sûreté aéroportuaire simultanément. VIGIE reste
dépendant d'un jeu de données local à construire (agent_reports
synthétiques + collecte Remote ID réelle une fois l'app testée) —
c'est un fait structurel du projet, pas une lacune de recherche.
