# Contribuer à VIGIE — guide d'accueil

> Pour toute personne qui rejoint le projet côté logiciel, quel que
> soit son niveau. Lire dans l'ordre : `docs/ARCHITECTURE.md` d'abord
> (comprendre le projet), ce document ensuite (comment contribuer).
> Terme pas clair (branche, Pull Request, framework...) ?
> [`docs/glossaire.md`](docs/glossaire.md) traduit tout en langage
> simple.

## Avant de coder

1. Lire `docs/ARCHITECTURE.md` en entier (10 minutes, aucun
   prérequis technique).
2. Regarder `schema/migration.sql` — c'est le contrat que tout le
   monde respecte. Ne jamais créer de table parallèle.
3. Si tu utilises Claude : charge le skill
   `.claude-skills/vigie-project/SKILL.md` (Settings > Capabilities >
   Skills sur claude.ai, ou colle son contenu en début de
   conversation) — il évite de devoir tout réexpliquer le contexte du
   projet à chaque session.
4. Si tu utilises Manus : les recherches vont dans `docs/`, jamais de
   code de production généré sans relecture humaine avant intégration.

## Règle n°1 — une tâche, un fichier, une personne

Deux personnes qui modifient le même fichier en parallèle créent des
conflits git à démêler, pire que si une seule personne l'avait fait.
Chaque tâche ci-dessous touche un périmètre de fichiers distinct —
rester strictement dedans. Pour toute modification hors périmètre,
demander d'abord.

## Règle n°2 — aucune décision d'architecture sans passer par Joe

Ajouter une fonctionnalité dans ton périmètre : librement. Changer le
schéma commun, l'architecture des couches (RF, classification,
corrélation), ou le scope du projet : jamais sans validation explicite
de Joe d'abord, même si ça semble être une amélioration évidente.

## Tâches disponibles

### Tâche A — Orchestrateur Supabase

**Fichiers** : nouveau fichier `src/pipeline/orchestrateur.py` uniquement.

**Objectif** : relier `src/classification/classifier.py` et
`src/correlation/correlation_engine.py` à la vraie base Supabase — lire
les événements au statut `nouveau`, les classifier, chercher les
corrélations, écrire les résultats.

**Point de départ** : le fichier `main()` du collecteur Sentinelle
(mentionné dans `docs/ARCHITECTURE.md`) suit exactement ce pattern —
lire, traiter, écrire, logguer. Ne pas réinventer la structure,
l'adapter.

**Prérequis** : Python de base (boucles, fonctions, imports). Les deux
modules à connecter sont déjà écrits et testables individuellement en
lançant `python src/classification/classifier.py` et
`python src/correlation/correlation_engine.py`.

### Tâche B — Dashboard amélioré

**Fichiers** : `src/dashboard/index.html` uniquement.

**Objectif** : ajouter une vue liste/timeline à côté de la carte
existante, un filtre par criticité ou par nature, un bouton de
rafraîchissement.

**Point de départ** : le fichier existant est autonome (HTML + JS,
bibliothèque Leaflet déjà utilisée pour la carte). Tester avec
`python src/simulate/generate_test_events.py` puis
`python -m http.server` dans `src/dashboard/`.

**Prérequis** : HTML/JS/CSS de base. Aucun framework à apprendre.

### Tâche C — Tests et scénarios de simulation

**Fichiers** : `src/simulate/` et nouveaux fichiers de test uniquement.

**Objectif** : enrichir `generate_test_events.py` avec plus de
scénarios réalistes (cas limites : événements simultanés au même
point, événements très espacés, doublons), et écrire quelques tests
simples pour vérifier que `correlation_engine.py` se comporte
correctement sur ces cas.

**Prérequis** : Python de base. Aucun risque de casser autre chose —
ce périmètre ne touche jamais le code de production.

## Comment livrer son travail

1. Créer une branche avec un nom clair (ex. `orchestrateur-supabase`).
2. Committer avec des messages descriptifs.
3. Ouvrir une Pull Request sur GitHub plutôt que pousser directement
   sur `main` — ça permet une relecture avant intégration, même
   rapide.
4. Tester localement avant d'ouvrir la PR (voir chaque tâche
   ci-dessus pour la commande de test).

## En cas de blocage

Décrire précisément : quel fichier, quelle commande lancée, quel
message d'erreur exact. Pas "ça ne marche pas" — "j'ai lancé X, j'ai
eu l'erreur Y à la ligne Z".
