# Journal de bord VIGIE

> Pour rattraper le projet en 5 minutes sans relire tout l'historique.
> Une entrée par session de travail significative, la plus récente en
> haut. Chaque entrée dit : ce qui a changé, pourquoi, et où le
> retrouver dans le repo.

---

## 30/08/2026 — Dossier officiel poussé sur le repo, README réorganisé

**Ce qui a changé :**
- Les 3 documents officiels (note conceptuelle, déclaration d'éthique,
  fiche de risques) sont maintenant **dans le repo**, pas seulement en
  téléchargement de chat — dossier [`dossier/`](../dossier/README.md),
  avec un statut clair des 8 pièces exigées par le règlement.
- Déclaration d'éthique et fiche de risques **redesignées** avec le
  logo VIGIE et la palette du site (accents ambre, niveaux de risque
  colorés plutôt qu'en texte brut).
- Un risque non pertinent retiré de la fiche (désistement d'un membre
  — l'équipe est à 4, marge d'un membre au-dessus du minimum
  réglementaire de 3 ; le signaler n'apportait rien).
- **README principal réorganisé** : l'ancienne liste plate de 16 liens
  devient des sections groupées (Pour commencer, Dossier officiel,
  Comprendre le projet, Volet matériel, Volet logiciel, Recherche) —
  navigation en tableaux, plus facile à parcourir pour un nouveau
  membre.
- Lien du site déployé ajouté dans la note conceptuelle :
  vigie.josephhounto.workers.dev

**Pourquoi :** les documents officiels vivaient uniquement dans les
téléchargements de chat — aucun membre de l'équipe ne pouvait y
accéder sans redemander. Le README, en s'enrichissant session après
session, était devenu une liste illisible.

**À faire ensuite :** lettre de présentation d'équipe, CV, confirmation
d'un encadrant — toujours les trois seules pièces manquantes du
dossier.

---

## 19/08/2026 — Équipe confirmée, statut de preuve, sécurité RLS

**La plus grosse nouvelle depuis le début du projet :** l'équipe est
**confirmée à 4 membres officiels** (Joe + 2 étudiants IAI Togo + 1
étudiant IPNET) — le risque n°1 suivi depuis le premier jour est levé.
CV et lettre de présentation en cours de rédaction par Joe avec Manus,
réunion prévue le 20/08.

**Ce qui a changé côté technique :**
- Nouveau champ `statut_preuve` dans le schéma commun
  (`mesure`/`rapporte`/`simule`/`externe`/`non_disponible`) — distingue
  enfin une donnée réellement mesurée d'une donnée de test, séparément
  du jugement IA (`nature`) et de l'état de traitement (`statut`).
- Alerte de sécurité ajoutée en tête de `schema/migration.sql` : les
  permissions actuelles sont pour le développement, pas pour la
  production — à corriger avant toute vraie connexion Supabase.
- Critères d'arrêt et rapport minimal ajoutés à `docs/protocole_test.md`.
- Nouveau `docs/ethique.md` — version courte et accessible des règles
  déjà présentes dans la déclaration formelle du dossier.
- GéoData Togo : confirmé que c'est une restriction d'accès, pas un
  bug — OurAirports reste la source de référence pour DXXX.

**Ce qui a été analysé mais volontairement pas intégré :** un lot de
11 documents Manus proposait de fragmenter la documentation en autant
de nouveaux fichiers. Sur relecture plus attentive (après retour
justifié de Joe sur un premier tri trop rapide), trois fichiers
avaient une vraie valeur non redondante et ont été intégrés :
`docs/contrat_evenement.md` (règles humaines du schéma), 
`docs/feuille_route.md` (échelle de maturité L0-L5 avec critères de
réussite), et l'extension des critères d'arrêt dans
`docs/protocole_test.md`. Les autres fichiers du lot (Idée générale,
Données VIGIE, Référentiels géographiques) étaient des reformulations
proches de nos propres documents existants — pas intégrés tels quels.

**Correction du jour :** l'affirmation "GéoData Togo bloqué" venait
d'un document Manus non vérifié indépendamment — corrigée dans
`docs/donnees.md` pour distinguer ce qui est réellement vérifié (site
en JavaScript pur, illisible par un outil automatisé) de ce qui reste
une affirmation non confirmée (restriction d'accès délibérée).

---

## 18/08/2026 (suite 2) — Firmware ESP32, fournisseurs, ARCEP, GéoData
  (qui est un émetteur, pas un récepteur — correction importante).
  Carte recommandée : Seeed XIAO ESP32-S3.
- Budget Couche 1 vérifié et documenté (`docs/materiel.md`) — Seeed
  Studio moins cher, DigiKey a un délai de 8 semaines à surveiller.
- Coordonnées ARCEP réelles obtenues (email, téléphone, adresse) —
  plus une hypothèse, une vraie voie de contact.
- GéoData Togo : catalogue "Aéroports" confirmé existant, présence de
  Lomé (DXXX) pas encore vérifiée par téléchargement direct.

**Pourquoi :** les 4 recherches Manus planifiées la dernière fois ont
toutes été traitées en un seul document bien structuré — la file
`docs/manus_recherches.md` est maintenant à jour.

**À faire ensuite :** rédiger la lettre à l'ARCEP ; commander les
cartes Seeed XIAO ESP32-S3 (deux, une de secours) une fois le budget
équipe confirmé.

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
