# Éthique et limites d'usage — ce que personne ne doit jamais faire

> Version courte, pour tous les contributeurs. La déclaration formelle
> du dossier de candidature (docx) dit la même chose en langage
> administratif — ce document-ci sert de rappel rapide, pas de
> remplacement.

## VIGIE est strictement passif

Le projet **écoute et signale**, il **n'agit jamais** sur un drone.
Aucune ligne de code, aucun montage matériel, ne doit jamais :
- émettre pour perturber un signal ou brouiller une fréquence,
- prendre le contrôle d'un drone,
- neutraliser un appareil,
- décoder le contenu d'une communication privée,
- déclencher automatiquement une action opérationnelle (fermeture de
  piste, alerte aux forces de l'ordre) sans validation humaine.

## Données minimales, toujours

Ne conserver que ce qui sert la démonstration : source, horodatage,
position générale, description, statut. Adresses MAC, identifiants
persistants, coordonnées précises d'une personne : supprimées ou
remplacées par un identifiant de session dès que possible.

## Ne jamais confondre preuve et supposition

- Une corrélation spatio-temporelle ne prouve pas qu'un lien existe.
- Une activité radio ne prouve pas la présence d'un drone.
- Un Remote ID reçu ne prouve pas d'intention malveillante.
- Le statut `a_verifier` est le repli par défaut en cas de doute —
  jamais une confiance excessive du modèle IA.

## Avant de connecter le projet à de vraies données (Supabase)

Voir l'avertissement en tête de `schema/migration.sql` — les
permissions actuelles sont volontairement ouvertes pour le
développement, **pas adaptées à une vraie mise en production**. Ne
jamais committer de clé API dans le code (HTML, JS, dépôt Git).

## Sur les tests terrain

Aucun essai autour d'un aérodrome actif, en particulier DXXX (Lomé),
sans coordination explicite avec les autorités compétentes. Voir
`docs/protocole_test.md` pour la procédure complète et les critères
d'arrêt.

## Ce que VIGIE n'est pas

Un outil de recherche et de prototypage étudiant — pas un système de
sûreté certifié, pas un remplacement du contrôle aérien ni des
autorités habilitées.
