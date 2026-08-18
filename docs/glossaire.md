# Glossaire — tous les termes techniques traduits en clair

> Si un mot dans un document VIGIE n'est pas expliqué sur place,
> il l'est ici. Classé par thème, pas par ordre alphabétique, pour
> pouvoir lire d'une traite.

## Le projet en général

- **API** : une façon standardisée pour deux programmes de se parler
  entre eux — comme un guichet où l'un dépose une demande et l'autre
  répond.
- **Cascade IA** : au lieu de dépendre d'un seul service d'intelligence
  artificielle, en essayer un premier, et si indisponible, basculer
  automatiquement sur un second — pour ne jamais tomber en panne
  complète.
- **Schéma commun** : la structure de données que toutes les sources
  d'information (agent, capteur) doivent respecter pour que le reste
  du système puisse les lire de la même façon.
- **Corrélation spatio-temporelle** : comparer des événements selon
  où et quand ils se sont produits, pour repérer si plusieurs
  événements séparés forment en fait un même phénomène.

## Le matériel radio (capteurs)

- **RF (radiofréquence)** : les ondes radio, celles utilisées par le
  WiFi, le Bluetooth, la téléphonie, et les télécommandes de drones.
- **SDR (radio logicielle)** : un récepteur radio générique dont le
  comportement est défini par un logiciel plutôt que par un circuit
  dédié à une seule fonction.
- **RTL-SDR** : un modèle de récepteur SDR bon marché, très répandu.
- **Downconverter** : un petit circuit qui "traduit" une fréquence
  radio trop haute pour un récepteur en une fréquence plus basse
  qu'il peut recevoir.
- **ESP32** : une petite carte électronique bon marché, capable de
  WiFi et Bluetooth, qu'on peut programmer facilement.
- **Firmware** : le programme qui tourne directement sur une carte
  électronique (comme un ESP32), pas sur un ordinateur classique.
- **Flasher** : installer un firmware sur une carte électronique —
  l'équivalent d'installer une application, mais sur une puce.
- **Remote ID** : un signal que certains drones diffusent volontairement
  pour annoncer leur position, comme une carte d'identité en vol.
- **WiFi Beacon** : un petit signal qu'un appareil WiFi émet en
  permanence pour signaler sa présence — les points d'accès WiFi le
  font en continu, et Remote ID réutilise ce mécanisme.
- **RSSI** : une mesure de la force d'un signal radio reçu, en général
  un nombre négatif (plus proche de zéro = signal plus fort).
- **Quart d'onde** : une longueur précise, calculée à partir d'une
  fréquence radio, utilisée pour dimensionner une antenne simple.

## Le code et GitHub

- **Repo (dépôt)** : l'espace où tout le code et les documents du
  projet sont rangés et suivis dans le temps.
- **Commit** : un "instantané" enregistré des changements faits à un
  moment donné, avec une description de ce qui a changé.
- **Push** : envoyer ses changements locaux vers le repo en ligne
  (GitHub), pour que tout le monde les voie.
- **Branche** : une copie de travail séparée du code, pour tester ou
  développer quelque chose sans toucher tout de suite à la version
  principale.
- **Pull Request (PR)** : une demande d'intégrer les changements d'une
  branche dans la version principale — permet à quelqu'un d'autre de
  relire avant que ce soit définitif.
- **Framework** : un ensemble d'outils tout prêts pour construire un
  programme plus vite, plutôt que tout écrire depuis zéro.
- **GitHub Actions** : un système qui exécute automatiquement du code
  selon un horaire ou un déclencheur, sans intervention humaine.
- **Stub** : une version simplifiée d'un morceau de code, qui montre la
  structure prévue mais qui doit encore être complétée.
- **Orchestrateur** : le morceau de code qui coordonne les autres —
  qui décide dans quel ordre faire les choses.

## L'infrastructure

- **Supabase** : le service en ligne qui héberge la base de données du
  projet (là où sont stockés tous les événements enregistrés).
- **Base de données / table** : l'endroit où l'information est rangée
  de façon structurée, en lignes et colonnes, comme un tableur.
