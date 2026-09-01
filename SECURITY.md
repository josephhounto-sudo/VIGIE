# Sécurité de VIGIE

VIGIE est un prototype de recherche et de démonstration. Il ne doit pas être
connecté à des données réelles de sûreté tant que l'authentification, les rôles,
la rétention et le journal d'audit ne sont pas validés avec l'institution partenaire.

## Principes actuels

- aucune clé API dans le dépôt ou dans le code client ;
- aucune écriture anonyme dans la base ;
- données simulées et externes identifiées par `statut_preuve` ;
- aucune neutralisation, émission ou prise de contrôle ;
- toute conclusion opérationnelle relève d'une personne habilitée.

## Signaler une vulnérabilité

Ne pas publier de donnée sensible dans une issue publique. Contacter d'abord le
mainteneur du dépôt avec une description minimale, les fichiers concernés et les
étapes de reproduction, sans inclure de clé ou de donnée personnelle.

## Avant un pilote réel

Le pilote devra au minimum ajouter : authentification, séparation lecture/écriture,
journal append-only des décisions, chiffrement des secrets, politique de rétention,
pseudonymisation des identifiants et revue du cadre ANAC/ARCEP/ASECNA.
