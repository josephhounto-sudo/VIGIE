# Contrat d'événement — règles en langage humain

> Le fichier `schema/migration.sql` définit la structure technique.
> Ce document explique les RÈGLES à respecter en le remplissant —
> ce que le SQL ne peut pas dire en un commentaire d'une ligne.
> S'applique à toute source : signalement agent, Remote ID, RF, ou
> tout import futur (FAA, RFUAV, etc.).

## Pourquoi ce contrat existe

Toutes les sources du projet doivent être converties vers le même
format `evenements`. C'est ce qui permet de comparer un signalement
agent, une observation Remote ID et un indice RF sans créer de tables
séparées qui ne se parlent pas entre elles.

## Champ par champ — la règle, pas juste le type

| Champ | Règle à respecter |
|---|---|
| `source_type` | Valeur contrôlée uniquement : `agent_terrain`, `remote_id`, `rf_drone`, ou une source externe explicitement documentée (ex. `test_faa_import`). Ne jamais inventer une nouvelle valeur sans la documenter ici. |
| `source_id` | Un identifiant de session suffit dans la plupart des cas. **Ne pas utiliser une identité persistante sans nécessité réelle** — c'est une règle de confidentialité, pas de commodité. |
| `titre` | Un résumé court. **Ne jamais présenter une hypothèse comme un fait** — "signature possible détectée", pas "drone détecté", tant que ce n'est pas confirmé. |
| `description` | Détails utiles uniquement. Aucun contenu privé, aucune donnée personnelle qui ne serait pas nécessaire à la démonstration. |
| `latitude` / `longitude` | Peuvent rester nulles si la position n'est pas disponible — **ne jamais inventer une coordonnée** à partir du nom d'une ville faute de mieux. |
| `horodatage` | Toujours en UTC. Conserver la précision réellement connue — ne pas arrondir pour faire plus propre. |
| `statut` | `nouveau`, `a_verifier`, `confirme`, `rejete` ou `clos`. `a_verifier` signifie qu'une décision humaine est nécessaire — **jamais qu'un drone est confirmé**. |
| `statut_preuve` | `mesure`, `rapporte`, `simule`, `externe` ou `non_disponible` — voir `schema/migration.sql` pour la définition complète de chaque valeur. Un événement sans ce champ rempli est un événement dont on ne sait pas d'où vient la confiance qu'on peut lui accorder. |

## Règles qui traversent tous les champs

- **Un indice RF ne devient jamais automatiquement un `incident_confirme`.** Le passage d'un statut à un autre plus grave exige une justification et, idéalement, une validation humaine.
- **Les sources externes restent externes.** Les données FAA et les cas réels (Gatwick, OR Tambo) gardent `statut_preuve = externe` — elles ne deviennent jamais des signalements togolais, même dans une démo.
- **La corrélation propose, elle ne décide pas.** Le moteur peut suggérer un lien entre deux événements ; un responsable humain confirme, corrige ou rejette ce lien. Voir `docs/ethique.md`.

## Compatibilité

Toute nouvelle source (une future collecte Android, un ESP32, une
chaîne RF) doit respecter ce contrat avant d'écrire dans `evenements`.
Ajouter un champ persistant ou modifier la structure de la table
nécessite une validation explicite de Joe avant intégration — même
règle que pour toute décision structurante.
