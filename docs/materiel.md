# Volet matériel — nomenclature capteur RF

> Vérifié par recherche (aout 2026) — pas une estimation en l'air.
> Sources : projets DIY documentés (RTL-SDR + Raspberry Pi, réception
> passive 2,4/5,8 GHz), dépôts open source (RF-Drone-Detection,
> SkyShield sur GitHub).

## Nomenclature de base

| Composant | Rôle | Budget indicatif | Statut |
|---|---|---|---|
| Dongle RTL-SDR | Réception RF large bande | ~25-30€ | À acheter |
| Antenne 2,4/5,8 GHz | Portée et sensibilité | ~10-15€ | À acheter |
| Raspberry Pi (ou réutilisation téléphone via OTG) | Traitement local du signal | Variable | À trancher selon budget équipe |
| Alimentation / boîtier | Déploiement terrain | ~5-10€ | Récupérable |

**Budget incompressible estimé : ~40-55€** hors Raspberry Pi (si réutilisation
d'un appareil déjà en main).

## Principe de fonctionnement (résumé)

Système strictement passif — réception uniquement, aucune émission,
donc aucune interférence avec le vol du drone ni avec le trafic
aéroportuaire réel. Le dongle scanne les bandes 2,4 GHz et 5,8 GHz où
opèrent les liaisons de commande et vidéo de la majorité des drones
grand public.

## Ce qui reste à vérifier avant le dossier de conception (30 sept)

- [ ] Réglementation togolaise sur l'écoute passive du spectre —
      aucune source vérifiée à ce stade, à ne pas supposer résolue.
- [ ] Modèle exact du dongle et de l'antenne à commander (dépend du
      budget final de l'équipe).
- [ ] Zone de test réelle pour valider la détection sur un vrai
      drone avant la démo de mars 2027.

## Limite à assumer explicitement dans le dossier

Un drone en vol totalement autonome, sans liaison radio active, est
invisible à ce système. Ne pas cacher cette limite — un jury de
régulateurs valorise la lucidité sur les limites plus qu'une
prétention de solution complète.
