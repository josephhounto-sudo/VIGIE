# VIGIE — Plateforme de corrélation d'événements de sûreté aéroportuaire

> Candidature CNISAI/AVSEC 2026 (ANAC Togo), catégorie Innovation libre.
> Squelette initial — structure fixée pour permettre le travail en parallèle
> de trois volets. Chaque volet peut avancer sans attendre les autres tant
> que le contrat de schéma (`schema/`) n'est pas modifié.

> **Tu reviens après une pause ou tu rejoins en cours de route ?**
> [`docs/journal.md`](docs/journal.md) — 5 minutes pour tout rattraper.
>
> **Nouveau dans l'équipe / non-développeur ?** Lis d'abord
> [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — aucune compétence
> technique requise.
>
> **Règles du concours ?** Voir
> [`docs/programme_concours.md`](docs/programme_concours.md) — calendrier,
> dossier requis, dotation.
>
> **Envie d'un exercice pratique à coût nul dès ce soir ?** Voir
> [`docs/guide_diy_reflecteur.md`](docs/guide_diy_reflecteur.md) — un
> réflecteur radio en carton et papier aluminium, protocole de mesure
> inclus. Démo pédagogique, pas le système de détection lui-même.
>
> **Tu utilises Claude sur ce projet ?** Le skill
> [`.claude-skills/vigie-project`](.claude-skills/vigie-project/SKILL.md)
> contient le protocole de travail (règles de push, triage des
> recherches Manus, conventions du schéma) — à installer une fois dans
> Claude pour ne pas le réexpliquer à chaque session.
>
> **Tu veux juste faire quelque chose de concret aujourd'hui, sans
> bagage technique ?** Va directement sur
> [`docs/guide_pratique_rf.md`](docs/guide_pratique_rf.md).
>
> **Tu rejoins le volet logiciel ?** Commence par
> [`CONTRIBUTING.md`](CONTRIBUTING.md) — tâches prêtes à prendre,
> scopées pour éviter tout conflit entre contributeurs.

> **Un mot technique pas clair ?** Tout est traduit dans
> [`docs/glossaire.md`](docs/glossaire.md).
>
> **Envie de voir à quoi ça ressemble en vrai ?**
> [`docs/cas_usage.md`](docs/cas_usage.md) — scénarios concrets.
>
> **Un exemple réel, pas hypothétique ?**
> [`docs/cas_reel_gatwick.md`](docs/cas_reel_gatwick.md) et
> [`docs/cas_reel_or_tambo.md`](docs/cas_reel_or_tambo.md) (cas africain).
>
> **Protocole avant un test terrain réel ?**
> [`docs/protocole_test.md`](docs/protocole_test.md).
>
> **Quelles données pour tester VIGIE ?**
> [`docs/donnees.md`](docs/donnees.md).
>
> **Prochaines recherches Manus à lancer ?**
> [`docs/manus_recherches.md`](docs/manus_recherches.md) — prompts prêts,
> priorisés.
>
> **Ce qu'il ne faut jamais faire ?**
> [`docs/ethique.md`](docs/ethique.md) — rappel court, pour tous.
>
> **Les règles exactes pour remplir un événement ?**
> [`docs/contrat_evenement.md`](docs/contrat_evenement.md).
>
> **Où en est chaque brique techniquement, vraiment ?**
> [`docs/feuille_route.md`](docs/feuille_route.md) — niveaux L0 à L5.

## Principe en une phrase

Collecter des signaux hétérogènes (signalement humain, alerte capteur RF),
les classer par nature/criticité via IA, les recouper dans le temps et
l'espace, et produire une carte de risque vivante + une traçabilité
décisionnelle — même architecture de résilience que Sentinelle (cascade
Groq → Gemini → repli), transposée à la sûreté aéroportuaire.

## Structure du repo

```
vigie/
├── schema/                  # LE CONTRAT — toute source doit produire du JSON conforme
│   └── migration.sql        # Schéma Supabase (tables + vue de risque)
├── src/
│   ├── capture/              # VOLET MATÉRIEL — capteur RF (RTL-SDR)
│   │   └── rf_capture_stub.py
│   ├── classification/       # VOLET LOGICIEL — cascade IA nature/criticité
│   │   └── classifier_stub.py
│   ├── correlation/          # VOLET LOGICIEL — recoupement temps/lieu
│   └── dashboard/            # VOLET LOGICIEL — carte de risque (à construire)
└── docs/
    └── materiel.md           # Nomenclature + budget capteur RF
```

## Qui touche quoi

- **Volet matériel** : uniquement `src/capture/`. Doit produire des
  événements conformes à `schema/migration.sql`, table `evenements`.
  N'a pas besoin de connaître la classification ni la corrélation pour
  avancer.
- **Volet logiciel** : `src/classification/`, `src/correlation/`,
  `src/dashboard/`. Peut développer et tester avec des événements
  simulés respectant le même schéma, sans attendre que le capteur RF
  physique existe.
- **Volet dossier** : ne touche pas le code. Référence ce repo dans la
  note conceptuelle comme preuve de structuration technique.

## Règle non négociable

Aucun code de neutralisation/brouillage. Le système s'arrête à
détection + alerte + traçabilité — cohérent avec le règlement du
concours (objets inertes uniquement) et avec le cadre légal (le
brouillage actif est réservé à des agences fédérales spécifiques dans
la plupart des juridictions consultées).

## Vibe coding

Comme pour Sentinelle : le code généré ici est un squelette à adapter,
pas un produit fini. Chaque stub contient des TODO explicites plutôt
que du faux détail qui donnerait une illusion d'avancement.
