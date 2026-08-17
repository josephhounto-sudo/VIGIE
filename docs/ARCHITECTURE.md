# VIGIE — Idée générale et architecture (à lire avant tout le reste)

> Ce document ne suppose aucune compétence technique. Si tu es dans
> l'équipe pour l'électronique, le dossier, ou la présentation orale,
> commence ici — pas par le code.

## L'idée en une phrase

Un aéroport reçoit en permanence de petits signaux d'alerte (un agent
qui remarque quelque chose, un drone qui vole où il ne devrait pas).
Aujourd'hui chacun est traité seul, sans lien avec les autres. VIGIE
les rassemble au même endroit, les trie automatiquement par gravité,
et **recoupe les signaux entre eux** pour révéler des schémas invisibles
à l'œil nu — par exemple si un même point génère anormalement plus
d'alertes à un moment donné.

## Le flux, en image simple

```
  Agent au sol signale        Capteur radio détecte
  un événement                un drone non-autorisé
        │                             │
        └───────────┬─────────────────┘
                     ▼
          CLASSIFICATION (IA)
     "de quoi s'agit-il, et c'est
        grave à quel point ?"
                     │
                     ▼
             CORRÉLATION
   "est-ce que ça ressemble à autre
    chose de récent, au même endroit ?"
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
   CARTE DE RISQUE        TRAÇABILITÉ
   vue d'ensemble en      historique + décision
      temps réel          pour chaque événement
```

## Les 5 blocs, expliqués simplement

| Bloc | Rôle en une phrase | Qui s'en occupe |
|---|---|---|
| Signalement agent | Un humain remonte un événement depuis le terrain | Volet logiciel (interface) |
| Capteur RF | Une petite radio écoute en permanence si un drone non-autorisé émet un signal à proximité | Volet matériel |
| Classification IA | Un modèle de langage lit chaque événement et décide : c'est confirmé, une fausse alerte, ou à vérifier | Volet logiciel |
| Corrélation | Le système compare les événements entre eux dans le temps et l'espace pour repérer des tendances | Volet logiciel |
| Carte de risque + traçabilité | La sortie finale : une vue d'ensemble pour un responsable, et un historique de chaque décision | Volet logiciel |

## Pourquoi c'est crédible techniquement

L'architecture de classification et de corrélation reprend un système
déjà en production depuis plusieurs semaines sur un autre projet
(Sentinelle) — on ne part pas d'une idée sur papier, on adapte un
moteur qui a déjà tourné en conditions réelles, avec ses leçons déjà
apprises (notamment : ne jamais dépendre d'un seul fournisseur d'IA,
toujours prévoir un mode de secours).

## Bonus pédagogique — à coût nul, dès ce soir

Un réflecteur radio en carton et papier aluminium, avec protocole de
mesure complet, pour illustrer la directivité RF devant le jury en
décembre. Guide complet : [`docs/guide_diy_reflecteur.md`](guide_diy_reflecteur.md).
Ce n'est pas le système de détection — juste une démonstration qui
montre que l'équipe comprend la physique du signal.

## Ce qui reste à construire (honnêtement, sans enjoliver)

- Le capteur RF physique — approche en deux couches désormais (voir
  [`docs/construction_rf.md`](construction_rf.md)) : Remote ID via ESP32
  (quelques euros, prouvé, prêt pour la démo) en priorité, détection
  d'énergie RF générique en extension si le temps le permet.
- La carte de risque — squelette fonctionnel désormais disponible (`src/dashboard/index.html`), teste avec les événements simulés ; reste à brancher sur Supabase pour devenir réellement "vivante".
- Vérification légale de l'écoute radio passive au Togo — pas encore faite (voir `docs/materiel.md`, synthèse déjà réunie, confirmation écrite ARCEP à obtenir avant tout test terrain).

## Sur l'automatisation

Le but à terme : que la classification et la corrélation tournent
**seules**, sans intervention manuelle, sur un rythme régulier —
exactement comme Sentinelle qui collecte automatiquement plusieurs
fois par jour via GitHub Actions (un robot qui exécute le code sur un
horaire fixe, gratuitement). Le squelette de cette automatisation est
déjà posé dans `.github/workflows/pipeline.yml`, prêt à être activé
dès que la classification et la corrélation seront fonctionnelles —
inutile de l'activer avant, ça échouerait pour rien.
