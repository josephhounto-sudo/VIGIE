# VIGIE — Plateforme de corrélation d'événements de sûreté aéroportuaire

> Candidature CNISAI/AVSEC 2026 (ANAC Togo), catégorie Innovation libre.

## 🚀 Pour commencer

| Besoin | Aller à |
|---|---|
| Rattraper le projet en 5 minutes | [`docs/journal.md`](docs/journal.md) |
| Comprendre VIGIE sans bagage technique | [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) |
| Voir la démonstration en ligne | [vigie.josephhounto.workers.dev](https://vigie.josephhounto.workers.dev/) |
| Un mot technique n'est pas clair | [`docs/glossaire.md`](docs/glossaire.md) |

## 📂 Dossier officiel de candidature

**Les documents à jour, prêts pour le dépôt, sont dans [`dossier/`](dossier/README.md)**
— statut de chacune des 8 pièces exigées par le règlement, avec liens
directs vers les fichiers Word. C'est le point d'entrée unique pour
tout ce qui concerne le dépôt.

## 🧭 Comprendre le projet en profondeur

| Besoin | Aller à |
|---|---|
| Voir le système en action (scénarios) | [`docs/cas_usage.md`](docs/cas_usage.md) |
| Un précédent réel (Gatwick, 2018) | [`docs/cas_reel_gatwick.md`](docs/cas_reel_gatwick.md) |
| Un précédent réel africain (OR Tambo) | [`docs/cas_reel_or_tambo.md`](docs/cas_reel_or_tambo.md) |
| Où en est chaque brique, par niveau de maturité (L0-L5) | [`docs/feuille_route.md`](docs/feuille_route.md) |
| Les règles pour remplir un événement | [`docs/contrat_evenement.md`](docs/contrat_evenement.md) |
| Ce qu'il ne faut jamais faire | [`docs/ethique.md`](docs/ethique.md) |
| Règles et calendrier du concours | [`docs/programme_concours.md`](docs/programme_concours.md) |

## 🔧 Volet matériel (RF / drones)

| Besoin | Aller à |
|---|---|
| Faire quelque chose de concret ce soir, sans bagage technique | [`docs/guide_pratique_rf.md`](docs/guide_pratique_rf.md) |
| Comprendre les choix RF (pourquoi) | [`docs/construction_rf.md`](docs/construction_rf.md) |
| Nomenclature et budget matériel | [`docs/materiel.md`](docs/materiel.md) |
| Protocole avant un test terrain réel | [`docs/protocole_test.md`](docs/protocole_test.md) |
| Exercice pédagogique à coût nul (réflecteur radio) | [`docs/guide_diy_reflecteur.md`](docs/guide_diy_reflecteur.md) |

## 💻 Volet logiciel — contribuer

| Besoin | Aller à |
|---|---|
| Tâches prêtes à prendre, sans conflit entre contributeurs | [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| Skill Claude (protocole de travail, à installer une fois) | [`.claude-skills/vigie-project`](.claude-skills/vigie-project/SKILL.md) |

## 🔍 Recherche et données

| Besoin | Aller à |
|---|---|
| Quelles données pour tester VIGIE | [`docs/donnees.md`](docs/donnees.md) |
| Prochaines recherches Manus à lancer | [`docs/manus_recherches.md`](docs/manus_recherches.md) |

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
