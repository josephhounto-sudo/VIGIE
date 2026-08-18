# Journal de bord VIGIE

> Pour rattraper le projet en 5 minutes sans relire tout l'historique.
> Une entrée par session de travail significative, la plus récente en
> haut. Chaque entrée dit : ce qui a changé, pourquoi, et où le
> retrouver dans le repo.

---

## 18/08/2026 (suite) — Interface de signalement agent

**Ce qui a changé :** l'interface graphique pour qu'un agent terrain
signale un événement existe maintenant (`src/interface/signalement.html`)
— formulaire mobile-first, géolocalisation en un clic, format conforme
au schéma commun. **Les 5 blocs du schéma ont désormais tous une
interface ou un code fonctionnel**, plus aucun n'est vide.

**Pourquoi :** c'était le seul bloc du schéma sans aucune interface —
la carte de risque affichait des événements, mais rien ne permettait
d'en créer un humainement.

**À faire ensuite :** brancher `ENVOI_URL` sur Supabase une fois les
clés configurées (même dépendance que le dashboard et l'orchestrateur).

---

## 18/08/2026 — Données, cas réels, protocole de test

**Ce qui a changé :**
- Le référentiel des 7 aéroports du Togo est chargé (`data/`) —
  coordonnées de Lomé vérifiées cohérentes avec le reste du projet.
- Un parseur transforme de vrais signalements de drones (données FAA)
  en événements au format VIGIE — preuve que le pipeline fonctionne sur
  de la donnée réelle, pas seulement simulée (`src/ingest/`).
- RFUAV (jeu de données RF pour la Couche 2) : licence vérifiée, mais
  1,3 To de données brutes — décision de ne pas l'utiliser tel quel,
  on passera par des modèles déjà entraînés si besoin.
- Deux cas réels documentés : Gatwick 2018 et OR Tambo (Johannesburg,
  2019/2023) — ce que VIGIE aurait changé, et ce qu'il n'aurait pas
  résolu, sans exagérer.
- Un protocole de test formel en 6 étapes, avec la liste complète des
  autorités togolaises à coordonner (ANAC, ARCEP, ASAIGE, ASECNA).

**Pourquoi :** analyse de plusieurs documents de recherche (Manus),
avec vérification indépendante des faits avant intégration.

**À retenir pour la suite :** OSM Togo (données cartographiques
détaillées) reste à charger — reporté après le 31 août, pas bloquant.

---

## 17-18/08/2026 — Décision RF finale et infrastructure du repo

**Ce qui a changé :**
- Architecture RF en deux couches tranchée : Remote ID (drones qui
  s'annoncent) en priorité, détection RF générique en extension —
  voir `docs/construction_rf.md`.
- Guide pratique sans prérequis technique créé
  (`docs/guide_pratique_rf.md`) — utilisable par n'importe qui, y
  compris pour tester ce soir sur un téléphone.
- Glossaire complet des termes techniques (`docs/glossaire.md`).
- `CONTRIBUTING.md` créé — 3 tâches prêtes pour des contributeurs
  logiciel de niveau L2.
- Skill Claude `vigie-project` versionné dans le repo
  (`.claude-skills/`).

**Pourquoi :** recentrage après plusieurs recherches sur le matériel
RF ; besoin d'accueillir des contributeurs sans tout réexpliquer à
chaque fois.

---

## Avant le 17/08/2026 — Fondations

- Concept VIGIE défini : corrélation d'événements de sûreté
  aéroportuaire (Innovation libre, CNISAI/AVSEC 2026).
- Schéma de données commun posé (`schema/migration.sql`).
- Premiers modules codés et testés : classification IA, moteur de
  corrélation, carte de risque (`src/`).
- Note conceptuelle et déclaration éthique rédigées pour le dossier de
  candidature.
