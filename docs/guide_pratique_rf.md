# Guide pratique — détecter un drone, sans expérience RF

> Pour qui : n'importe qui dans l'équipe, même sans aucune notion de
> radiofréquence, d'électronique ou de réseau. Aucun terme technique
> n'est utilisé sans être expliqué.
> Pour comprendre POURQUOI ces choix, voir `docs/construction_rf.md`.
> Ce document-ci répond seulement à COMMENT faire, étape par étape.

## Ce qu'on essaie de faire, en une phrase

Beaucoup de drones du commerce annoncent en permanence "je suis là,
voici ma position" — un peu comme un avion qui annonce sa position en
vol. On veut construire un petit appareil qui écoute cette annonce et
la note. C'est tout ce que fait la partie "matériel" du projet, dans
sa version la plus simple.

---

## Étape 1 — Tester ça dès aujourd'hui, sans rien acheter

Tu as déjà tout ce qu'il faut : un smartphone Android.

1. Ouvre le Play Store sur le téléphone.
2. Cherche l'application **"OpenDroneID"** (ou "Open Drone ID
   Receiver" selon la version disponible). C'est une application
   gratuite, publiée par un projet open source reconnu (voir
   `docs/construction_rf.md` pour la source exacte).
3. Installe-la et ouvre-la. Elle va demander l'autorisation d'accéder
   au WiFi/Bluetooth et à la position — normal, c'est comme ça qu'elle
   capte les annonces des drones.
4. Laisse l'application ouverte quelques minutes, si possible à
   l'extérieur ou près d'une fenêtre.
5. **Note ce qui se passe** : rien détecté ? Un drone apparaît ? Un
   message d'erreur ? Toute observation compte, même "rien ne s'est
   passé" — ça nous dit si le téléphone lui-même a une limite technique.

**Rien à installer d'autre, rien à souder, rien à acheter pour cette
étape.** Si ça fonctionne, on a déjà un point de départ pour le vrai
capteur du projet.

### Ce que ce test NE fait PAS (pour éviter toute confusion)

- Il ne détecte **que** les drones qui acceptent de s'annoncer. Un
  drone qui ne veut pas être vu n'apparaîtra pas — c'est une vraie
  limite du projet, pas un bug du test.
- Ce n'est **pas** la même chose qu'une application comme WiFiAnalyzer
  ou NetSpot — celles-là servent à autre chose (voir étape 3) et ne
  détecteront jamais un drone.

---

## Étape 2 — Construire un capteur dédié (une fois l'étape 1 validée)

Si le test au téléphone fonctionne, l'étape suivante est une petite
carte électronique appelée **ESP32** (quelques euros, en vente en
ligne). Elle fait la même chose que le téléphone, mais en continu, sans
mobiliser un smartphone.

Ce qu'il faut concrètement :
1. Acheter une carte ESP32 (n'importe quel modèle de base convient).
2. La brancher à un ordinateur par câble USB.
3. Installer un programme déjà écrit par d'autres (pas besoin de
   l'écrire soi-même) — voir `docs/construction_rf.md` pour les liens
   exacts vers ces programmes.
4. "Envoyer" ce programme sur la carte (ça s'appelle "flasher" —
   l'équivalent d'installer une application, mais sur une puce plutôt
   qu'un téléphone).

Aucune compétence en électronique n'est nécessaire pour cette étape —
seulement suivre une notice, comme installer un logiciel. La seule
compétence utile est d'être à l'aise avec une ligne de commande
(taper des instructions dans un terminal) ; ça s'apprend en une
après-midi si personne dans l'équipe ne le sait déjà.

---

## Étape 3 — Un petit exercice complémentaire (facultatif, pédagogique)

Ce n'est **pas** une partie du détecteur de drone. C'est un exercice à
part qui aide à comprendre comment un signal radio se comporte — utile
pour la présentation devant le jury, pas pour la détection elle-même.

**Ce qu'il faut** (tout est déjà chez toi ou récupérable) :
- Un morceau de carton rigide (environ 30 x 20 cm)
- Du papier aluminium
- Du ruban adhésif
- Un smartphone avec l'application gratuite **WiFiAnalyzer** (à ne pas
  confondre avec OpenDroneID de l'étape 1 — rôle différent)

**Comment faire** :
1. Courber le carton en forme de coquille douce (comme la moitié d'un
   bol), sans le plier brutalement.
2. Recouvrir le côté creux avec le papier aluminium, bien lissé.
   Attacher avec du ruban au dos. Ne rien laisser toucher une antenne
   ou une prise du routeur.
3. Placer ce réflecteur derrière l'antenne du routeur WiFi de l'équipe,
   à environ 3-5 cm de distance, face creuse tournée vers la zone que
   tu veux tester.
4. Sur le téléphone, ouvrir WiFiAnalyzer et noter la force du signal
   (affichée en général comme un nombre négatif, ex. "-65") du réseau
   de l'équipe, 5 fois de suite.
5. Tourner le réflecteur d'un petit angle, refaire 5 mesures.
   Recommencer 3-4 fois avec des angles différents.
6. Comparer : le nombre le "moins négatif" (ex. -58 est meilleur que
   -70) indique la meilleure orientation.

**Règle de sécurité simple** : on ne mesure que le réseau WiFi de
l'équipe elle-même, jamais celui d'un voisin ou d'un inconnu.

---

## Ce qu'il ne faut jamais faire (pour toute l'équipe, sans exception)

- Ne jamais essayer de "décoder" ou lire le contenu d'un réseau qui
  n'appartient pas à l'équipe.
- Ne jamais construire quoi que ce soit qui **émet** un signal pour
  perturber ou bloquer un drone — le projet écoute uniquement, il
  n'agit jamais sur les drones.
- En cas de doute sur si une action est autorisée : demander avant de
  faire, pas après.

## Si quelque chose ne marche pas

Note précisément : quel appareil, quelle étape, quel message d'erreur
exact. "Ça ne marche pas" ne suffit pas pour qu'on puisse t'aider —
"j'ai ouvert l'app, elle demande une permission que je ne trouve pas
dans les réglages" permet d'agir tout de suite.
