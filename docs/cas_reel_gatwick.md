# Un cas réel : ce que VIGIE aurait changé à Gatwick (2018)

> Contrairement à `docs/cas_usage.md` (scénarios illustratifs), ce
> document s'appuie sur un événement réel et documenté — pour ancrer
> le projet dans un précédent vérifiable, pas une hypothèse.

## Ce qui s'est passé

Entre le 19 et le 21 décembre 2018, l'aéroport de Gatwick (Londres) a
fermé sa piste unique pendant environ 30 heures suite à des
signalements répétés de drones à proximité de l'aire de vol. Bilan :
environ 1 000 vols annulés ou déroutés, 140 000 passagers affectés,
plus de 15 millions de livres de pertes pour la seule compagnie
easyJet. Aucun drone n'a jamais été physiquement retrouvé ni identifié
avec certitude.

## Trois failles précises dans la gestion de l'incident

### 1. Des signaux dispersés, jamais recoupés en un tableau unique

Les témoignages ont montré une activité par "groupes" répartis sur
trois jours, en douze occurrences distinctes, chacune durant de 7 à
45 minutes. Chaque signalement (agent de sécurité, pilote, policier)
était traité au moment où il arrivait, sans vue d'ensemble consolidée
montrant le motif de récurrence en train de se former.

### 2. Deux sources en désaccord, jamais réconciliées formellement

La police continuait d'affirmer la présence de drones sur la base de
témoignages visuels, pendant que les systèmes radar de l'armée de
l'air (RAF) n'en détectaient aucun. La coordination entre ces deux
sources d'information n'a réellement commencé que dans l'après-midi du
troisième jour.

### 3. Une arrestation injustifiée, faute de traçabilité claire

Un couple a été arrêté et détenu 36 heures, alors qu'il ne possédait
aucun drone et se trouvait au travail au moment des signalements. Un
règlement à l'amiable de 55 000 £ leur a été versé après coup. Rien
dans le dossier ne permettait de confronter rapidement leur situation
aux événements réellement enregistrés.

## Ce que VIGIE aurait concrètement changé

| Faille observée | Réponse apportée par VIGIE |
|---|---|
| Signaux dispersés sur 3 jours, 12 occurrences séparées | Chaque signalement entre dans la même table d'événements ; le moteur de corrélation détecte le motif de récurrence (même zone, créneaux répétés) dès les toutes premières occurrences, pas après coup |
| Désaccord police / radar militaire jamais réconcilié | Les deux types de source (visuelle, technique) alimentent le même système ; un désaccord entre elles devient une anomalie explicitement affichée sur la carte de risque, à trancher activement, plutôt que deux versions parallèles non coordonnées |
| Arrestation injustifiée faute de traçabilité | L'historique complet (traçabilité) permet de vérifier en quelques secondes si une personne ou un lieu donné correspond réellement à un événement enregistré, plutôt que de se fier à un témoignage isolé non recoupé |

## Ce que VIGIE n'aurait probablement PAS changé — honnêteté avant tout

**Le drone lui-même n'aurait probablement pas été intercepté ni
formellement identifié par le Système 1 (Remote ID).** Tout indique
qu'il s'agissait d'un drone piloté délibérément pour perturber
l'aéroport — un tel appareil n'a aucune raison de diffuser son
identité. C'est exactement le scénario que le Système 2 (détection
d'énergie RF générique, non encore construit) viserait à couvrir, et
qui reste une limite assumée du projet à ce stade (voir
`docs/construction_rf.md`).

**La contribution réelle et défendable de VIGIE dans ce cas n'est donc
pas "on aurait attrapé le drone"** — c'est la coordination des signaux
humains et techniques, et la protection contre une décision
précipitée fondée sur un signal isolé non vérifié. C'est déjà une
valeur concrète et mesurable (un couple innocent, 36 heures de
détention, 55 000 £ de règlement), sans avoir besoin d'exagérer ce que
le système peut faire.

## Sources

- Wikipédia — Gatwick Airport drone incident
- BBC News — couverture de l'incident et des suites
- The Guardian — reportage détaillé sur le déroulé et l'enquête
- Déclarations publiques de Sussex Police (2018-2020)

Faits vérifiés par recherche web le 18/08/2026. Aucun élément de ce
document n'est une supposition — chaque faille listée correspond à un
fait rapporté par une source publique.
