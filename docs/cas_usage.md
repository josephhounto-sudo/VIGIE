# Cas pratiques d'utilisation

> Pour comprendre à quoi VIGIE ressemble concrètement, en usage réel —
> pas seulement en théorie. Chaque scénario montre un ou plusieurs
> blocs du système en action. Termes techniques traduits dans
> [`docs/glossaire.md`](glossaire.md).

## Scénario 1 — Un drone conforme est repéré (cas normal, Système 1)

Un livreur amateur fait voler un drone grand public à proximité de la
zone aéroportuaire, sans intention hostile. Le drone diffuse son
Remote ID (sa "carte d'identité en vol") en continu, parce que ce modèle
est compatible avec le protocole.

1. Le capteur du Système 1 capte cette diffusion.
2. Un événement est créé : position, heure, identifiant du drone.
3. La classification IA l'analyse : rien d'alarmant dans le contexte,
   nature classée "anomalie" avec une criticité basse.
4. L'événement apparaît sur la carte de risque, sans déclencher
   d'alerte urgente.
5. Le responsable sûreté le voit passer dans son suivi de routine, sans
   avoir besoin d'agir dans l'immédiat.

**Ce que ça démontre** : le système absorbe le bruit de fond (drones
inoffensifs) sans noyer l'opérateur sous de fausses urgences.

## Scénario 2 — Deux signalements distincts, un seul vrai problème (corrélation)

En l'espace de deux heures, un agent signale un comportement suspect
près de la clôture nord, puis un autre agent signale, sans le savoir,
un accès badge irrégulier au même secteur.

1. Les deux événements entrent séparément dans le système.
2. Chacun est classé individuellement — aucun des deux, seul, ne
   semble critique.
3. Le moteur de corrélation détecte que les deux se sont produits au
   même endroit et à un intervalle rapproché.
4. Un lien est créé automatiquement, avec un score de confiance, et
   remonté ensemble sur la carte de risque plutôt que noyés séparément
   dans une longue liste.

**Ce que ça démontre** : c'est la valeur ajoutée centrale de VIGIE —
deux signaux faibles, isolés, deviennent un signal fort une fois
recoupés. Aucun agent seul n'aurait vu le lien.

## Scénario 3 — Une fausse alerte est écartée (l'IA ne dit pas oui à tout)

Le capteur RF détecte une signature qui ressemble à un drone, mais qui
provient en réalité d'un appareil WiFi domestique dans un bâtiment
proche de la clôture.

1. L'événement est créé avec les caractéristiques du signal.
2. La classification IA l'examine et, faute d'éléments concordants
   (pas de mouvement caractéristique, signal fixe), le classe
   `fausse_alerte_probable` avec une justification prudente.
3. Un responsable examine les éléments et décide de rejeter ou non la
   relation. La proposition et le verdict restent dans l'historique.

**Ce que ça démontre** : le système ne cherche pas à maximiser le
nombre d'alertes. L'IA aide à prioriser ; elle ne clôt pas le dossier.

## Scénario 4 — Un drone qui refuse de s'identifier (limite assumée du Système 1)

Un drone survole la zone sans diffuser aucun Remote ID — volontairement
désactivé, ou modèle non conforme.

1. Le Système 1 ne voit rien : c'est sa limite connue, documentée dans
   `docs/construction_rf.md`, pas un bug caché.
2. Seul le Système 2 (écoute RF générique, une fois construit)
   pourrait repérer une émission radio suspecte même sans identité
   déclarée.

**Ce que ça démontre** : pourquoi le projet documente explicitement
cette limite plutôt que de prétendre à une couverture totale — et
pourquoi le Système 2 reste un objectif, pas un détail secondaire.

## Scénario 5 — Une identité annoncée ne correspond pas au signal réel (piste d'innovation)

Un Remote ID est reçu, annonçant un drone à une position donnée — mais
si un capteur du Système 2 existe déjà à ce stade, il pourrait un jour
détecter que le signal radio réel ne vient pas exactement de cette
position, ou que sa signature ne correspond pas au modèle annoncé.

**Statut** : piste d'innovation non construite à ce stade (voir
`docs/construction_rf.md`), présentée ici pour illustrer une direction
future, pas une fonctionnalité actuelle.

## Scénario 6 — Le responsable sûreté commence sa journée

Avant l'ouverture du terminal, le responsable sûreté consulte la carte
de risque plutôt que plusieurs rapports séparés (agents, capteurs,
mails).

1. Il voit en un coup d'œil les zones où des événements se sont
   accumulés dans les dernières 24h.
2. Il clique sur un point pour voir l'historique complet d'un
   événement : quand il a été détecté, comment il a été classé,
   s'il a été confirmé ou écarté.
3. Il décide où concentrer une ronde de vérification, sur la base de
   données recoupées plutôt que de sa seule intuition.

**Ce que ça démontre** : VIGIE ne remplace pas la décision humaine — il
la nourrit avec une vue d'ensemble qu'aucun canal séparé ne peut
donner seul.
