# État du prototype VIGIE

Ce document est la référence courte entre le site, le code et les pièces de
candidature. Il doit être mis à jour lorsqu'une preuve nouvelle est ajoutée.

## Niveaux

| Niveau | Définition | État au 1er septembre 2026 |
|---|---|---|
| L0 | Scénario structuré, contrat de données, limites explicites | Atteint |
| L1 | Briques logicielles exécutables et tests reproductibles | Partiellement atteint |
| L2 | Réception Remote ID réelle documentée | Non atteint |
| L3 | Essai autorisé avec partenaire et scénario contrôlé | Non atteint |
| L4 | Pilote intégré avec métriques et gouvernance | Non atteint |
| L5 | Déploiement opérationnel validé | Non atteint |

## Ce qui fonctionne aujourd'hui

- le schéma commun d'événement ;
- la transformation d'une ligne FAA fournie au parseur ;
- la corrélation déterministe de scénarios géolocalisés et horodatés ;
- le repli prudent de la classification lorsque les services IA sont absents ;
- la génération reproductible d'événements simulés ;
- la démonstration web du parcours de vérification et de décision humaine.

## Ce qui reste à prouver

- la réception Remote ID avec le matériel retenu ;
- la portée et le taux de perte en conditions contrôlées ;
- la corrélation à partir d'identifiants persistants ou de trajectoires ;
- l'orchestration complète avec une base sécurisée ;
- la persistance append-only des décisions ;
- les performances sur un jeu étiqueté ;
- l'utilité et le délai gagné lors d'un essai institutionnel.

## Règle de communication

Chaque affirmation publique doit être classée dans l'une de ces catégories :

- **implémenté et testé** : commande et test présents dans le dépôt ;
- **démontré** : parcours reproductible avec données simulées ;
- **externe** : information issue d'une source publiée ;
- **prévu** : capacité conçue mais non encore prouvée ;
- **non disponible** : preuve ou autorisation absente.

Une intention ne doit jamais être présentée comme une mesure terrain.
