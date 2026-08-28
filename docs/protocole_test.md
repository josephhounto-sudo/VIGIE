# Protocole de test — avant tout essai terrain réel

> S'applique une fois le prototype Couche 1 assemblé, avant toute
> sortie sur le terrain. Non nécessaire pour le dépôt du 31 août — à
> respecter avant le dossier de conception du 30 septembre.

## Autorités togolaises à coordonner (liste complète)

Au-delà de l'ANAC déjà identifiée, quatre autorités peuvent être
concernées selon le contexte du test :

- **ANAC** — autorisation de principe, analyse de risques.
- **ARCEP** — régulation des fréquences (déjà documenté dans
  `docs/materiel.md`).
- **ASAIGE** — sûreté aéroportuaire.
- **ASECNA / ATC** — coordination avec le contrôle aérien si le test a
  lieu à proximité d'un aérodrome actif.

Accord écrit de l'ANAC obligatoire avant tout essai ; ASECNA/ATC,
ASAIGE et ARCEP à solliciter selon le contexte précis du test.

## Les 6 étapes

1. **Autorisation et responsable désigné** — obtenir l'accord écrit,
   nommer une personne responsable du test.
2. **Vérification du terrain** — hors zone sensible, coordonnées du
   site communiquées aux autorités si requis localement.
3. **Réception statique avant décollage** — vérifier que le système
   capte le Remote ID du drone de test, et qu'il n'enregistre aucune
   donnée tierce inutile.
4. **Vols courts et planifiés** — noter uniquement "reçu / non reçu /
   incertain", jamais convertir l'essai en évaluation de portée
   opérationnelle réelle.
5. **Comparaison journal / observation** — confronter les données
   reçues à l'observation directe de l'équipe, supprimer les données de
   test après la période autorisée.
6. **Rapport de limites** — documenter honnêtement : protocoles
   effectivement reçus, défaillances, événements non corrélés, mesures
   correctives envisagées.

## Critères d'arrêt — arrêter le test et documenter l'échec si...

- Le lieu n'est pas autorisé ou hors du cadre coordonné.
- Le matériel ne correspond pas à la configuration annoncée.
- La source de données contient des informations personnelles non
  nécessaires (identifiants, position précise d'un tiers).
- Le résultat n'est pas reproductible dans les mêmes conditions.
- Une action d'émission, de brouillage, de prise de contrôle ou de
  neutralisation est envisagée à quelque titre que ce soit — sortir
  immédiatement du protocole, ce n'est plus un test VIGIE.

## Rapport minimal attendu après chaque test

Date, version du code/de l'application utilisée, description du
matériel, données d'entrée, sorties obtenues, erreurs rencontrées,
résultats négatifs (pas seulement les succès), limites constatées, et
une décision explicite : poursuivre, corriger, suspendre ou abandonner.

## Garde-fou permanent

Le test est **hors opérations aéronautiques réelles**, sur un drone
appartenant à l'équipe uniquement. Aucun automatisme de fermeture de
piste ou d'appel à des moyens de neutralisation, quel que soit le
résultat du test.

## Référence académique comparable

Le Cyber Defence Campus (HSLU) documente un projet universitaire
similaire — plateforme de preuve de concept de surveillance Remote ID
par WiFi, explicitement présentée comme non destinée à la production.
Bon parallèle à citer devant le jury : VIGIE n'est pas seul dans cette
démarche, et la prudence affichée est cohérente avec l'état de l'art
académique du domaine.

## Sources

- FAA — UAS Detection, Mitigation, and Response on Airports (23/06/2025)
- OACI — Protection de l'infrastructure de l'aviation civile contre les
  aéronefs non habités (2023)
- ANAC Togo — page Drones (espace professionnel)
- Cyber Defence Campus / HSLU — Drone Remote ID Monitoring System
