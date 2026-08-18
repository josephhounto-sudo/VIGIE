# Référentiel géographique — aéroports du Togo

> Chargé le 18/08/2026 depuis OurAirports (mirroir officiel GitHub
> `davidmegginson/ourairports-data`, domaine public, sans garantie
> d'exactitude — voir `docs/materiel.md` pour le rappel des limites).
> Fichiers mondiaux volumineux (85 000+ aéroports) filtrés au Togo
> uniquement pour rester léger dans le repo.

## Fichiers

| Fichier | Contenu | Lignes |
|---|---|---|
| `togo_airports.csv` | Les 7 aéroports du Togo, coordonnées incluses | 7 |
| `togo_airport_frequencies.csv` | Fréquences radio associées | 5 |
| `togo_runways.csv` | Pistes | 2 |
| `togo_regions.csv` | Subdivisions administratives togolaises | 6 |
| `countries.csv` | Référentiel mondial des codes pays (léger, gardé entier — nécessaire pour interpréter `iso_country`) | 250 |

## Les 7 aéroports du Togo

| Code | Type | Nom | Ville | Latitude | Longitude |
|---|---|---|---|---|---|
| DXXX | Aéroport international | Lomé–Tokoin International Airport | Lomé | 6,16561 | 1,25451 |
| DXNG | Aéroport international | Niamtougou International Airport | Niamtougou | 9,76668 | 1,09094 |
| DXAK | Petit aéroport | Akpaka Airport | Atakpamé | 7,583 | 1,117 |
| DXDP | Petit aéroport | Djangou Airport | Dapaong | 10,80042 | 0,24237 |
| DXKP | Petit aéroport | Kolokope Airport | Anié | 7,80345 | 1,29597 |
| DXMG | Petit aéroport | Sansanné-Mango Airport | Mango | 10,37301 | 0,47138 |
| DXSK | Petit aéroport | Sokodé Airport | Sokodé | 8,99428 | 1,15300 |

**Vérification de cohérence** : les coordonnées de Lomé (DXXX) correspondent
exactement aux coordonnées déjà utilisées par défaut dans
`src/dashboard/index.html` et `src/simulate/generate_test_events.py` —
aucune correction nécessaire.

## Limite à assumer

Ce référentiel donne la position des aéroports, pas les limites de
sûreté (clôtures, zones tampons, périmètres réglementaires). Pour ça,
il faudrait le portail officiel `geodata.gouv.tg` ou une demande directe
à l'ANAC — non fait à ce stade (catalogue non exploré, voir notes de
recherche).

## OSM Togo (Geofabrik) — non chargé, bloqué techniquement

Le téléchargement direct depuis `download.geofabrik.de` n'est pas
accessible depuis l'environnement d'exécution de Claude (domaine hors
liste autorisée). Deux options pour Joe :
1. Télécharger manuellement le GeoPackage Togo depuis
   `download.geofabrik.de/africa/togo.html` et l'uploader dans une
   prochaine session pour intégration.
2. Se contenter d'`togo_airports.csv` pour le MVP — largement
   suffisant pour la démonstration, l'extrait OSM complet
   (bâtiments, routes, zones urbaines) n'est nécessaire que pour une
   version enrichie de la carte de risque.

Non bloquant pour le 31 août.
