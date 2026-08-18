---
name: vigie-project
description: "Contexte et protocole de travail pour le projet VIGIE (candidature CNISAI/AVSEC 2026, ANAC Togo) — plateforme de corrélation d'événements de sûreté aéroportuaire (Remote ID drones + signalement agent). Utiliser CE SKILL dès que la conversation mentionne VIGIE, CNISAI, AVSEC, ANAC, le repo GitHub josephhounto-sudo/VIGIE, une recherche Manus sur le RF/RTL-SDR/drone/Remote ID pour ce projet, ou toute question liée au concours. Couvre : le protocole de triage des recherches Manus (repérer redondance, distinguer coût-nul réel vs illusoire, vérifier les sources), la règle d'approbation avant tout push de décision structurante, le pattern de push Git sécurisé (token masqué), et les conventions du schéma commun du repo. Déclencher aussi si l'utilisateur colle un document/PDF/pptx de recherche sans préciser le projet mais que le contenu porte sur RTL-SDR, downconverter, drone detection, ou sûreté aéroportuaire."
---

# VIGIE — protocole de travail

## Contexte en une phrase

VIGIE est le projet de Joseph "Joe" Hounto (étudiant en médecine, Lomé,
freelance design+IA) pour le concours CNISAI/AVSEC 2026 de l'ANAC Togo
(catégorie Innovation libre) : une plateforme qui ingère des signaux
hétérogènes (signalement agent, détection de drone), les classe par IA,
les corrèle dans le temps/l'espace, et produit une carte de risque —
architecture dérivée du projet Sentinelle de Joe (même pattern de
cascade IA résiliente).

**Avant toute chose : lire `docs/journal.md`.** C'est le journal de
bord — la façon la plus rapide de savoir où en est réellement le
projet, plus fiable que ce résumé statique qui peut dater. Ce fichier
SKILL.md décrit le protocole de travail (stable), le journal décrit
l'état actuel (change à chaque session).

Repo : `github.com/josephhounto-sudo/VIGIE` (public).
Documents de référence dans `docs/` : `programme_concours.md` (règlement),
`ARCHITECTURE.md` (accessible non-développeurs), `guide_pratique_rf.md`
(comment faire, sans prérequis), `construction_rf.md` (décisions
matériel RF), `glossaire.md` (tous les termes techniques traduits),
`cas_usage.md` + `cas_reel_gatwick.md` + `cas_reel_or_tambo.md`
(scénarios et précédents réels), `protocole_test.md` (avant tout essai
terrain), `donnees.md` (bases de données évaluées et chargées),
`manus_recherches.md` (file de prompts Manus planifiés).
`CONTRIBUTING.md` liste les tâches ouvertes pour contributeurs logiciel.

## Règle n°1 — ne jamais pousser de décision structurante sans accord explicite

Joe a explicitement posé cette règle après plusieurs push d'affilée sans
repasser par lui. Toute **décision structurante** (choix d'architecture,
pivot technique, changement de scope, budget) doit être présentée en
conversation et validée avant tout `git push`. Les corrections mineures
et purement factuelles sourcées peuvent continuer normalement, mais en
cas de doute sur ce qui compte comme "structurant", demander plutôt que
supposer.

## Protocole de triage d'une recherche Manus

Joe fait régulièrement des recherches via Manus et colle le résultat
(PDF, pptx, markdown, ou app web complète) dans la conversation. À
chaque nouveau document :

1. **Vérifier la redondance avant tout.** Comparer avec les recherches
   précédentes dans la conversation ou dans `docs/`. Si le contenu
   répète une conclusion déjà établie sous un autre format, le dire
   explicitement plutôt que de re-analyser comme si c'était neuf — et
   signaler la redondance à Joe (Manus a une fenêtre gratuite limitée,
   ne pas la laisser se gaspiller en reformulations).
2. **Distinguer "coût nul démontré" de "coût nul qui n'aboutit pas".**
   Les recherches sur le DIY radio ont montré un piège récurrent :
   un objet gratuit (antenne, réflecteur) est confondu avec une solution
   complète alors qu'il ne remplace ni le tuner ni la conversion de
   fréquence. Toujours vérifier si la conclusion finale est "ça marche"
   ou "ça aide un composant qui existe déjà".
3. **Croiser avec ce qui est déjà écrit dans le repo** (`docs/`) avant
   d'écrire un nouveau document — éviter la duplication qui a déjà eu
   lieu sur les 3 documents "coût nul" (PDF, md, pptx).
4. **Ne jamais confondre un outil zéro-coût pour UN usage avec un outil
   zéro-coût pour le VRAI besoin.** Exemple concret déjà rencontré :
   WiFiAnalyzer est zéro-coût pour comparer son propre routeur, mais ne
   sert à rien pour détecter un drone — l'app correcte pour ça est
   `opendroneid/receiver-android`. Toujours vérifier que l'outil
   recommandé répond à la question posée, pas à une question voisine.
5. **Présenter une synthèse critique, jamais une paraphrase.** Ce que
   Manus rapporte doit être confronté aux décisions déjà prises dans
   le repo, pas simplement résumé.

## État des 5 blocs (vérifier `docs/journal.md` pour l'état le plus à jour)

Au 18/08/2026, les cinq blocs du schéma ont tous une interface ou du
code fonctionnel — plus aucun n'est vide : signalement agent
(`src/interface/signalement.html`), capteur RF (stubs Remote ID +
générique), classification IA (code réel, attend les clés API),
corrélation (code réel, testé), carte de risque (squelette testé).
Ne jamais supposer qu'un bloc est encore un stub sans vérifier le repo
— l'état change vite.

## Protocole de recherche Manus

Les recherches Manus sont désormais planifiées à l'avance dans
`docs/manus_recherches.md`, avec des prompts prêts et une contrainte de
format explicite dans chaque prompt (éviter la dérive de scope déjà
observée — un site web complet livré à la place d'un tableau markdown).
Un prompt à la fois, jamais deux recherches en parallèle sans lien.

## Architecture RF retenue

Deux couches, ne jamais les confondre :
- **Couche 1 — Remote ID (ESP32 ou app Android existante)** : détecte
  les drones conformes qui diffusent leur identité (ASTM F3411 /
  OpenDroneID). Coût quasi nul, MVP prioritaire.
- **Couche 2 — Énergie RF générique (downconverter DIY)** : détecte
  tout émetteur 2,4 GHz, y compris un drone non-conforme. Plus coûteux
  et plus risqué techniquement, extension si le temps le permet.

La Couche 1 ne nécessite AUCUNE des solutions "downconverter" étudiées
dans les recherches RF génériques — ne pas gater son avancement sur la
résolution de la Couche 2.

## Pattern de push Git (repo VIGIE)

Le token GitHub, quand Joe le fournit, ne doit **jamais** être répété
dans le texte de réponse. Utiliser ce pattern (déjà validé sur ce
projet) :

```bash
GH_TOKEN='<token>'
GH_USER='josephhounto-sudo'
REPO='VIGIE'
cd /home/claude/vigie_push
git remote set-url origin "https://x-access-token:${GH_TOKEN}@github.com/${GH_USER}/${REPO}.git"
git push -q origin main
git remote set-url origin "https://github.com/${GH_USER}/${REPO}.git"
unset GH_TOKEN
```

Toujours retirer le token du remote juste après le push. Toujours
tester le code (exécution locale) avant de committer — plusieurs bugs
(calibration de la corrélation, sous-tirage de la chaîne RF) ont déjà
été détectés par ce test avant push, pas après.

## Conventions du schéma commun (`schema/migration.sql`)

Toute nouvelle source de données doit produire un événement conforme à
la table `evenements` (source_type, source_id, titre, description,
latitude, longitude, horodatage, statut) — jamais créer une table
parallèle. C'est le contrat qui permet aux volets matériel et logiciel
d'avancer sans se bloquer mutuellement.

## Ton et méthode attendus

Joe a explicitement demandé un rôle de conseiller brutalement honnête :
challenger les suppositions, ne jamais valider sans base, appliquer un
prémortem avant tout lancement, et faire un cycle interne V1 → critique
→ V2 avant de livrer une réponse (ne jamais montrer le V1 ou le
processus). Pas de remplissage, pas de louanges non méritées.
