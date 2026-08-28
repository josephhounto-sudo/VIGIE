# Feuille de route — par niveau de maturité technique

> Complète le calendrier de la note conceptuelle (dates : 15 août,
> 30 septembre, décembre). Ce document répond à une autre question :
> **jusqu'où chaque brique est-elle réellement prouvée**, indépendamment
> de la date. Utile pour ne jamais présenter un objectif comme un
> résultat déjà acquis.

## Objectif

Construire une chaîne passive, traçable et reproductible pour
organiser des événements de sûreté autour de Lomé/DXXX — sans jamais
présenter une capacité de déploiement opérationnel réel avant
validation technique et réglementaire complète.

## Les niveaux, avec critère de réussite

| Niveau | Contenu | Critère de réussite | Statut au 19/08/2026 |
|---|---|---|---|
| **L0** | Données synthétiques, signalement agent, démonstration hors ligne | Les événements sont conformes au contrat commun, heures en UTC, coordonnées contrôlées, statuts valides | Prêt — `src/interface/signalement.html` + générateur de test fonctionnels |
| **L1** | Normalisation, classification prudente, corrélation, affichage | Le rapprochement utilise une fenêtre documentée, explique son résultat, ne transforme jamais une proximité en confirmation | Prototype local fonctionnel — testé |
| **L2** | Réception Remote ID réelle sur Android | Sessions enregistrées avec appareil, date, lieu général, qualité, résultat — données personnelles inutiles supprimées | Prêt à tester, non encore prouvé — voir `docs/guide_pratique_rf.md` |
| **L3** | Évaluation d'une carte ESP32 | Carte, firmware, câblage, sortie et limites documentés avant toute comparaison | Dépend de l'obtention réelle du matériel (Seeed XIAO ESP32-S3, voir `docs/materiel.md`) |
| **L4** | RF générique avec chaîne complète | Pipeline lit les formats disponibles, distingue signal et bruit, résultat qualifié explicitement de laboratoire | Extension expérimentale, non prioritaire |
| **L5** | Scénario avec drone partenaire, contexte autorisé | Scénario planifié, coordonné, supervisé, rapporté — aucune décision opérationnelle automatisée | Conditionnel — dépend d'un partenaire et des autorisations (`docs/protocole_test.md`) |

## Critère d'arrêt transversal (tous niveaux)

Arrêter et documenter l'échec plutôt que de forcer un résultat si : le
lieu n'est pas autorisé, le matériel ne correspond pas à la
configuration annoncée, la source contient des données personnelles
non nécessaires, le résultat n'est pas reproductible, ou qu'une action
d'émission/brouillage/neutralisation est envisagée — voir les critères
complets dans `docs/protocole_test.md`.

## Ordre de développement — pourquoi Remote ID d'abord

Remote ID passe en premier parce qu'il produit les premières données
réelles et valide le modèle commun d'événement sans dépendre d'un
matériel RF complexe. La RF générique reste dans la même architecture,
mais elle vient après : elle dépend d'une chaîne complète (antenne,
filtrage, conversion, récepteur adapté) plus longue à assembler et à
valider.

## Critères de passage entre niveaux

Un niveau ne passe au suivant que si ses résultats sont
**reproductibles, documentés, et accompagnés de résultats négatifs**
— pas seulement des succès.

Trois règles non négociables, quel que soit le niveau atteint :
- Une absence de réception Remote ID ne doit jamais être convertie en
  "absence de drone confirmée".
- Un indice RF ne doit jamais être converti en "drone confirmé".
- Une corrélation ne devient jamais une décision automatique — voir
  `docs/contrat_evenement.md`.

## Ce que le pilote conceptuel doit montrer

Un événement reçu ou saisi → sa normalisation → son statut → son
rapprochement éventuel avec un autre événement → l'explication de ce
rapprochement → la validation humaine. **Pas** une couverture
universelle, **pas** une capacité d'intervention.

## Dépendances actuelles

| Brique | Dépend de |
|---|---|
| Test Android (L2) | Modèle exact du téléphone disponible, source Remote ID autorisée pour le test |
| ESP32 (L3) | Carte réellement obtenue (commande ou prêt) |
| RF générique (L4) | Matériel, caractérisation, essais contrôlés |
| Scénario partenaire (L5) | Partenaire drone identifié, autorisations obtenues |
| Backend réel | Correction des politiques de sécurité SQL (voir alerte en tête de `schema/migration.sql`) |

La candidature du 31 août revendique principalement **L0 et L1**, déjà
prouvés. L2 à L5 restent explicitement conditionnels dans le dossier —
ne jamais les présenter comme acquis.
