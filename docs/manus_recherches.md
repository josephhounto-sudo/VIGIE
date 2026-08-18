# File de recherches Manus — planifiée à l'avance

> Fenêtre gratuite Manus : jusqu'au 25/08/2026. Chaque prompt ci-dessous
> inclut une contrainte de format explicite ("tableau markdown
> uniquement") — leçon tirée d'une recherche précédente qui a produit un
> site web complet au lieu d'un tableau, gaspillant du temps de fenêtre
> gratuite.
>
> **Statut au 18/08/2026 : les 4 prompts ci-dessous sont traités.**
> Manus a livré un document unique respectant le format demandé.
> Résultats intégrés dans `docs/construction_rf.md` (firmware Mesh-Mapper
> retenu), `docs/materiel.md` (budget ESP32), `docs/donnees.md` (GéoData
> Togo, catalogue "Aéroports" confirmé), et ce document (ARCEP, ci-dessus).
> Prochaine file à définir une fois ces intégrations exploitées.

## Règle d'usage

Un prompt à la fois. Vérifier et intégrer le résultat précédent avant
de lancer le suivant — jamais deux recherches en parallèle sans lien
entre elles.

## Priorité 1 — Urgent (débloquent une action concrète cette semaine)

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

## Priorité 2 — Utile avant le 30 septembre, pas avant le 31 août

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

## Une fois un résultat reçu

Coller le résultat dans la conversation Claude avec ce qui doit en
être fait (vérifier, intégrer dans tel document, ignorer) — jamais
intégré tel quel sans relecture, comme pour toutes les recherches
précédentes.
