# Guide DIY — réflecteur passif et mesure RSSI (démonstration pédagogique)

> Contenu extrait et organisé depuis les recherches Manus du 17/08/2026
> (PDF, guide markdown, pptx "SIGNAL/ZÉRO"). Statut : démonstration
> pédagogique pour la présentation de décembre — ne fait PAS partie du
> système de détection VIGIE lui-même. Voir `docs/construction_rf.md`
> pour l'architecture RF réelle (Remote ID + RF générique).

## Pourquoi ce guide existe

Un exercice de directivité RF à coût nul, utile pour montrer au jury
que l'équipe comprend la physique du signal avant de coder — mais ce
n'est ni un détecteur de drone, ni un composant du système VIGIE.

## Applications Android nécessaires (aucune, root non requis)

| Application | Rôle | Bandes | Statut |
|---|---|---|---|
| **WiFiAnalyzer (VREM)** | Choix principal : points d'accès, courbes de canaux, puissance dans le temps, export | 2,4/5/6 GHz selon matériel | Open source, gratuit |
| NetSpot | Relevé visuel de couverture, comparaison de réseaux | 2,4/5/6 GHz annoncé | Scanner gratuit, heatmaps payantes |
| WiFiman (Ubiquiti) | Complémentaire si routeur UniFi | Dépend de l'infrastructure | Gratuit |

**Installer WiFiAnalyzer en premier** — c'est le seul nécessaire pour le protocole ci-dessous.

⚠️ **Rappel** : ces applications ne détectent PAS de drone (voir
`docs/construction_rf.md`). Elles ne servent qu'à comparer le RSSI du
propre point d'accès de l'équipe.

## Matériaux (récupération, coût nul)

| Élément | Réemploi possible | Dimension de départ |
|---|---|---|
| Support | Carton rigide (emballage) | 30 × 20 cm |
| Surface réfléchissante | Papier aluminium | Même surface que le carton |
| Entretoise | Bouchon, carton plié, pince | 3-5 cm d'écart initial |
| Gabarit | Papier + crayon, ou contour d'un bol/bouteille | Demi-parabole approximative |

## Construction — 4 étapes

1. **Courber le carton** en demi-parabole douce (~30×20 cm), sans pliure aiguë qui casserait la surface réfléchissante.
2. **Lisser l'aluminium** sur la face concave, fixer au dos avec du ruban — aucun métal ne doit toucher l'antenne ou les ports du routeur.
3. **Placer derrière l'antenne** à orienter, concavité vers la zone à favoriser, en commençant à 3-5 cm entre l'antenne et le sommet du réflecteur.
4. **Tourner par pas de 10-15°**, relever à chaque position, ne changer qu'un seul paramètre entre deux séries de mesures.

**À ne pas faire** : couvrir la ventilation du routeur, forcer les antennes, toucher les ports, transformer le réflecteur en émetteur.

## Protocole de mesure RSSI

| Étape | Action | Donnée à noter | Limite |
|---|---|---|---|
| 1. Référence | Figer routeur/téléphone/point de mesure, relever 5× sans réflecteur | RSSI, bande, canal, heure | Le RSSI varie naturellement — une mesure unique est insuffisante |
| 2. Réflecteur | Changer uniquement l'orientation du réflecteur | Même série de 5 valeurs | Améliore une direction, peut en dégrader une autre |
| 3. Comparaison | Comparer les **médianes**, jamais un pic isolé | Écart médian en dB | Ni une mesure de gain calibrée, ni un spectre complet |

Exemple de feuille de relevés (dBm) :

| Position | M1 | M2 | M3 | M4 | M5 | Médiane |
|---|---|---|---|---|---|---|
| Référence (sans réflecteur) | -66 | -65 | -67 | -66 | -65 | -66 |
| 0° | -62 | -61 | -62 | -63 | -61 | -62 |
| 15° | -64 | -63 | -64 | -65 | -63 | -64 |
| 30° | -66 | -65 | -67 | -66 | -66 | -66 |

Règle de lecture : le RSSI le moins négatif est le signal le plus fort.

## Ce que ce démonstrateur prouve, et ce qu'il ne prouve pas

**Prouve** : le principe physique qu'une surface réfléchissante peut
rediriger l'énergie RF dans l'espace (une étude Dartmouth rapporte
jusqu'à +6 dB / -10 dB, mais avec des formes optimisées imprimées en
3D — pas garanti avec une feuille de carton artisanale).

**Ne prouve pas** : un gain calibré, une mesure de spectre complète, ou
quoi que ce soit lié à la détection de drone. Le présenter uniquement
comme exercice illustratif de directivité RF.

## Cadre légal (identique au reste du projet)

Mesurer uniquement le point d'accès de l'équipe, avec autorisation.
Aucune capture de trame, aucun décodage, aucune identification ou
journalisation de réseau tiers.

## Sources

- WiFiAnalyzer (VREM), NetSpot Android, Ubiquiti WiFiman — pages officielles, consultées le 17/08/2026
- Android Developers — Wi-Fi scanning overview, consulté le 17/08/2026
- Dartmouth DartNets Lab — WiPrint (BuildSys 2017), consulté le 17/08/2026
- Texas Instruments — AN058 Antenna Selection Guide, consulté le 17/08/2026
- RTL-SDR Blog V4 Datasheet, consulté le 17/08/2026

Recherche menée via Manus, organisée et vérifiée par Claude avant intégration.
