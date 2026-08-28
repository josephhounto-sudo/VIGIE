# File de recherches Manus — planifiée à l'avance

> Fenêtre gratuite Manus : jusqu'au 25/08/2026. Chaque prompt ci-dessous
> inclut une contrainte de format explicite ("tableau markdown
> uniquement") — leçon tirée d'une recherche précédente qui a produit un
> site web complet au lieu d'un tableau, gaspillant du temps de fenêtre
> gratuite.
>
> **Statut au 18/08/2026 : la file du 18/08 (firmware, fournisseurs,
> ARCEP, GéoData) est traitée** — voir `docs/journal.md` pour le résumé.
> Nouvelle file ci-dessous, à lancer maintenant.

## Règle d'usage

Un prompt à la fois. Vérifier et intégrer le résultat précédent avant
de lancer le suivant — jamais deux recherches en parallèle sans lien
entre elles.

## File active (18/08/2026, 2e vague)

### Priorité 1 — Installation Mesh-Mapper sur Xiao ESP32-S3

```
Trouve les instructions précises d'installation et de flashage du
firmware Mesh-Mapper (drone-mesh-mapper, github.com/colonelpanichacks/
drone-mesh-mapper) spécifiquement sur une carte Seeed XIAO ESP32-S3 :
outils requis (Arduino IDE, PlatformIO, esptool.py), étapes de
compilation, câblage éventuel, erreurs fréquentes rapportées dans les
issues GitHub. Réponds en liste d'étapes markdown uniquement, pas
d'application, pas de site web.
```

### Priorité 1 — Accès réel à GéoData Togo (prompt révisé le 19/08)

```
Le site geodata.gouv.tg est une application JavaScript pure (confirmé
par test direct) — un simple fetch ne peut pas afficher son contenu.
Ouvre le site dans un vrai navigateur, va sur la couche "Aéroports -
Établissements", et inspecte les requêtes réseau déclenchées au
chargement des données (onglet réseau/network de l'inspecteur) pour
identifier l'endpoint API réel utilisé en coulisses. Teste cet
endpoint directement et vérifie si l'aéroport de Lomé (DXXX) y figure.
Réponds en tableau markdown uniquement, avec l'URL exacte de
l'endpoint trouvé.
```

### Priorité 2 — Portée réelle rapportée (Mesh-Mapper / OpenDroneID)

```
Cherche des retours d'expérience réels (issues GitHub, forums,
discussions) sur la portée de détection effective de Mesh-Mapper et de
l'application OpenDroneID Receiver Android — pas les chiffres annoncés
par les développeurs, mais des mesures ou témoignages d'utilisateurs
en conditions réelles. Note les écarts entre portée annoncée et portée
observée. Réponds en tableau markdown uniquement.
```

## Archive — file du 18/08/2026 (1ère vague, traitée)

Un prompt à la fois. Vérifier et intégrer le résultat précédent avant
de lancer le suivant — jamais deux recherches en parallèle sans lien
entre elles.

### Priorité 1 — Urgent (débloquent une action concrète cette semaine)

### Firmwares Remote ID pour ESP32

```
Compare 3 à 4 firmwares/logiciels open source de réception Remote ID
(ASTM F3411/OpenDroneID) compatibles ESP32 : opendroneid-core-c,
ArduRemoteID, Mesh-Mapper, et tout autre projet actif trouvé. Pour
chacun : facilité d'installation (flashage), documentation disponible,
compatibilité avec un ESP32 générique (pas un modèle propriétaire),
activité de maintenance récente (dernier commit). Réponds en tableau
markdown uniquement, pas d'application, pas de site web.
```

### Fournisseurs ESP32 vers le Togo

```
Trouve 3 à 5 fournisseurs qui livrent une carte ESP32 de base jusqu'au
Togo (Lomé), avec prix en euros ou FCFA, délai de livraison estimé, et
mode de paiement accepté (USDT, carte Visa, virement). Réponds en
tableau markdown uniquement, même format que la recherche RTL-SDR
précédente.
```

### Priorité 2 — Utile avant le 30 septembre, pas avant le 31 août

### Catalogue GéoData Togo

```
Explore le portail geodata.gouv.tg : quelles couches géographiques
sont disponibles, sous quels formats (WMS, WFS, téléchargement
direct), et est-ce que des données autour de l'aéroport de Lomé (DXXX)
y figurent ? Réponds en tableau markdown uniquement.
```

### Procédure de confirmation légale ARCEP

```
Cherche la procédure exacte pour obtenir une confirmation écrite de
l'ARCEP Togo sur l'écoute radio passive du spectre 2,4 GHz par une
équipe étudiante — formulaire, contact, délai habituel. Réponds en
tableau markdown uniquement.
```

### Une fois un résultat reçu

Coller le résultat dans la conversation Claude avec ce qui doit en
être fait (vérifier, intégrer dans tel document, ignorer) — jamais
intégré tel quel sans relecture, comme pour toutes les recherches
précédentes.
