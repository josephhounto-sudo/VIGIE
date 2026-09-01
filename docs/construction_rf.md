# Construction RF — décision finale (deux couches)

> Mis à jour le 17/08/2026. Remplace entièrement la version précédente
> (qui ne considérait que la voie downconverter). Toujours aucun chiffre
> de budget définitif ici — voir `docs/materiel.md` une fois confirmé.

## Décision : deux couches complémentaires, pas une seule technologie

### Couche 1 — Réception Remote ID (MVP, à construire en premier)

Dans les cadres américain et européen, de nombreux drones récents doivent
diffuser des informations d'identification et de position en WiFi ou
Bluetooth — norme ASTM F3411 / OpenDroneID. Cette obligation ne doit pas
être transposée automatiquement au parc togolais. Un microcontrôleur ESP32
peut recevoir ces diffusions compatibles sans chaîne RF additionnelle.

- Coût : accessible, carte ESP32 seule, sans chaîne RF additionnelle.
- Firmware recommandé pour la réception : **Mesh-Mapper**
  (drone-mesh-mapper), activement maintenu, licence MIT, exporte les
  détections en CSV/KML/GeoJSON. Supporte explicitement les cartes
  Seeed XIAO ESP32-C3 (WiFi seul) et XIAO ESP32-S3 (WiFi + Bluetooth —
  couverture plus large, recommandée). ArduPilot/ArduRemoteID est un
  **émetteur** (utile pour un drone de test qui diffuse son propre
  Remote ID), pas un récepteur — ne pas confondre les deux rôles.
  `esp32-c3-remote-id` écarté : son propre dépôt indique qu'il est
  cassé et prévu à la suppression.
- Portée : variable selon l'appareil, le protocole, l'antenne et
  l'environnement. VIGIE ne publiera une valeur qu'après mesure documentée.
- Aucune compétence RF/soudure requise — flashage de firmware existant.

**C'est la voie retenue pour la première validation matérielle.**

### Couche 2 — Détection d'énergie RF générique (objectif d'extension)

Voir la voie downconverter déjà documentée (Ian Wraith / SUP-2400,
bande 2,4 GHz). Détecte tout émetteur 2,4 GHz, y compris un drone
délibérément non conforme qui ne diffuse aucun Remote ID.

- Statut : DIY à construire, plus complexe, risque d'échec plus élevé.
- Rôle : extension si le temps et les compétences de l'équipe le
  permettent après la couche 1. Non indispensable pour un premier
  prototype fonctionnel.
- **Confirmation croisée (3 recherches indépendantes, 17/08/2026)** :
  aucune solution à coût matériel nul n'existe pour cette couche. Un
  objet gratuit (antenne, réflecteur) ne remplace ni le tuner, ni la
  conversion de fréquence — le RTL-SDR V4 plafonne à 1,766 GHz, un
  downconverter reste incontournable. Ce n'est plus à revérifier.

## Pourquoi deux couches, et pas une seule — limite assumée sans détour

Le Remote ID identifie les drones **coopératifs**. Un acteur hostile n'a
aucune raison de le diffuser, et des outils existent déjà pour le
falsifier (un projet identifié génère de faux signaux Remote ID pour
simuler plusieurs drones fictifs). Présenter Remote ID seul comme une
solution de sûreté serait trompeur devant un jury de régulateurs — ce
n'est qu'une brique de conscience de trafic légitime. La couche 2 est
ce qui répond réellement au scénario de menace (drone non coopératif).

**Angle d'innovation supplémentaire, à explorer une fois la couche 1
stable** : un écart entre l'identité Remote ID annoncée et la signature
RF réelle observée (couche 2) est lui-même un signal d'anomalie
exploitable — détection de spoofing. Non prioritaire avant le 31 août,
mais à garder en tête pour le dossier de conception du 30 septembre.

## Intégration au schéma commun

Aucun changement de schéma nécessaire. Le Remote ID est un
`source_type` de plus dans la table `evenements` (ex. `remote_id`),
au même titre que `rf_drone` (couche 2) et `agent_terrain`. L'architecture
à sources multiples posée dès le départ absorbe cette découverte sans
refonte.

## Rappel légal (inchangé)

Réception seule dans les deux couches, jamais de décodage de contenu de
réseau tiers hors du protocole Remote ID lui-même (qui est un protocole
public de diffusion, pas une communication privée). Confirmation écrite
ARCEP toujours recommandée avant tout test terrain réel.

## Ce qui reste ouvert

- Choix définitif du firmware de réception Remote ID à adapter (parmi
  les projets identifiés) — à trancher une fois un ESP32 en main.
- La couche 2 (downconverter) reste conditionnée au profil recruté
  (STM32/SPI ou soudure CMS).

## Test à coût nul de la Couche 1 — faisable cette semaine

Contrairement à la Couche 2, la Couche 1 peut être testée **avant même
d'acheter un ESP32** : le protocole Remote ID est une diffusion
publique (pas une communication privée), recevable par l'application
open source `opendroneid/receiver-android`, installable directement sur
un téléphone déjà possédé.

**Point d'attention à ne pas manquer** : ne pas confondre avec les
applications de scan WiFi grand public (WiFiAnalyzer, NetSpot,
WiFiman) — utiles pour comparer un routeur, mais elles ne décodent pas
les trames Remote ID. Seule une application dédiée OpenDroneID convient
pour ce test.

**Inconnue restante** : le modèle exact de l'Infinix de Joe n'est pas
vérifié pour le support WiFi NAN / la cadence de scan Bluetooth
nécessaires. Le test lui-même (installer l'app et observer) est le
moyen le plus rapide de lever cette inconnue — moins cher que toute
recherche supplémentaire.

## Méthodologie de mesure réutilisable (pour la calibration future de la Couche 2)

Protocole validé par plusieurs sources concordantes, à réutiliser tel
quel une fois un capteur Couche 2 construit : position fixe, 5 relevés
par configuration, comparer les médianes (jamais un pic isolé), ne
changer qu'un seul paramètre entre deux séries. Un réflecteur passif
(carton + papier aluminium) peut aussi servir de démonstration
pédagogique de directivité pour la présentation de décembre — à
présenter explicitement comme un exercice illustratif, jamais comme un
composant du système de détection lui-même.
