# Construction RF DIY — faisabilité et choix de portée

> Analyse du 17/08/2026, basée sur une recherche sourcée (Manus, vérifiée
> par Claude). Document séparé de `docs/materiel.md` — ne contient aucun
> chiffre de budget, volontairement, en attente de confirmation.

## Décision de portée : 2,4 GHz uniquement pour la démonstration

Aucune source consultée ne présente un montage RTL-SDR pour 5,8 GHz qui
soit à la fois complet, publiquement vérifiable et reproductible.
L'architecture théorique (5,8 GHz − 5 GHz OL = 800 MHz FI) est plausible
mais systématiquement qualifiée de "projet avancé à valider au banc" par
les sources techniques les plus sérieuses (EEVblog, MyriadRF).

**VIGIE cible donc exclusivement la bande 2,4 GHz** pour le prototype et
la démonstration — bande la plus utilisée pour le lien de commande de la
majorité des drones grand public. Ce n'est pas un renoncement mais un
choix de portée assumé, à documenter explicitement dans le dossier de
conception : couverture de la bande la plus répandue et la mieux
prouvée, plutôt qu'une promesse de couverture totale non tenable dans
le calendrier du concours.

## Deux voies DIY documentées pour 2,4 GHz

### Voie principale recommandée — 24DownConvert (Ian Wraith)

Translation ~2,45 GHz → ~1,45 GHz (dans la plage native du RTL-SDR V4),
via mélangeur ADL5350 et oscillateur local ADF4350 piloté par STM32.

- Reproductibilité : élevée — dépôt GitHub complet, câblage SPI
  documenté, résultat rapporté sur Wi-Fi/Zigbee/Bluetooth/ISM.
- Compétence requise : STM32 + bus SPI (firmware).
- Source : github.com/IanWraith/24DownConvert, corroboré par rtl-sdr.com.

### Voie alternative — SUP-2400 modifié (KD0CQ)

Conversion d'un tuner satellite DirecTV SUP-2400 par modification CMS.

- Reproductibilité : moyenne — plusieurs réplications indépendantes
  confirmées (détection Wi-Fi à 2,447 GHz, clavier sans fil à 2,465 GHz),
  mais résultat sensible à la qualité de soudure et au filtrage.
- Compétence requise : soudure de composants montés en surface (CMS).
- Avantage : compatible avec l'approche "matériaux de récupération" du
  reste du projet, si un tuner DirecTV peut être trouvé/récupéré.
- Source : kd0cq.com (tutoriel), corroboré par plusieurs réplications
  communautaires sur rtl-sdr.com.

## Conséquence directe sur le recrutement

Ce choix technique précise le profil à chercher en priorité pour le
volet matériel : une personne ayant déjà manipulé un microcontrôleur
(STM32, Arduino ou ESP32) et idéalement un bus SPI — pas seulement
"électronique" en général.

## Rappel légal (déjà établi dans docs/materiel.md)

Réception seule, jamais de décodage de contenu de réseau tiers, mesure
agrégée d'occupation/puissance uniquement. Confirmation écrite ARCEP à
obtenir avant tout test terrain réel (non bloquant pour le 31 août).

## Ce qui reste ouvert

- Choix final entre les deux voies : dépend du profil recruté et du
  matériel réellement disponible (tuner DirecTV à récupérer ou non).
- Aucun chiffrage budgétaire dans ce document — voir `docs/materiel.md`
  une fois la voie choisie et confirmée.
