# Volet matériel — nomenclature capteur RF

> Mis à jour le 17/08/2026 après recherche croisée (Manus + vérification
> Claude). Remplace la version précédente — l'ancienne sous-estimait la
> chaîne technique nécessaire.

## ⚠️ Correction critique par rapport à la première version

**Un RTL-SDR classique (V3/V4, jusqu'à ~1,766 GHz) ne reçoit PAS
directement les bandes 2,4 GHz et 5,8 GHz où opèrent les drones.** La
chaîne complète nécessite :

```
Antenne 2,4/5,8 GHz -> filtre -> downconverter -> RTL-SDR (bande couverte)
                        (ex. 2,45 GHz -> 450 MHz, ou 5,8 GHz -> 800 MHz)
```

Sans le downconverter, le dongle seul ne capte rien d'utile sur les
bandes drone. À intégrer dans le budget et dans la note conceptuelle.

## Dimensions d'antenne (monopole quart d'onde, calcul de référence)

| Bande | Longueur d'onde | Quart d'onde | Longueur pratique (facteur 0,96) |
|---|---|---|---|
| 2,400 GHz | 12,49 cm | 3,12 cm | 3,00 cm |
| 2,450 GHz | 12,24 cm | 3,06 cm | 2,94 cm |
| 2,4835 GHz | 12,07 cm | 3,02 cm | 2,90 cm |
| 5,150 GHz | 5,82 cm | 1,46 cm | 1,40 cm |
| 5,800 GHz | 5,17 cm | 1,29 cm | 1,24 cm |

Une antenne DIY (fil de cuivre coupé à ces longueurs) est viable pour un
prototype de test — cohérent avec l'approche "matériaux de récupération"
du reste du projet.

## Fournisseurs — vérifiés le 17/08/2026, aucun en confiance "Élevée" pour Lomé

| Fournisseur | Produit | Prix observé | Couvre 2,4/5,8 GHz directement | Confiance livraison Lomé | Note |
|---|---|---|---|---|---|
| Ubuy Togo | JEOZBM RTL-SDR (100 kHz-1,766 GHz) | 51 253 FCFA (~78€) | Non | Moyenne | Site localisé TG, paiement Visa/Mastercard/PayPal visible, frais/douane au checkout |
| AliExpress | RTL-SDR Blog V4 seul | 22,57€ | Non | À confirmer | Prix/délai dépendent du vendeur et de l'adresse |
| eBay (rtl-sdr-blog) | RTL-SDR Blog V3 | 34,95 USD + 3 USD port (~32€) | Non | À confirmer | "Worldwide" annoncé, Togo non testé |
| RTL-SDR Blog (officiel) | V4 + kit antenne générique | 39,95 USD (~37€) | Non (kit non dédié) | À confirmer | Article de lancement 2023, prix non garanti actuel |
| ~~Passion Radio~~ | V4 | 49,67€ | — | Exclu | Livraison exclut explicitement la plupart de l'Afrique, dont le Togo |

**Budget révisé** : dongle (~25-40€) + antenne DIY (récupération) +
filtre/downconverter (à chiffrer, non inclus dans les prix ci-dessus)
= environ 50-70€ hors frais de douane/livraison, à confirmer au
checkout pour chaque fournisseur.

## Réglementation — synthèse vérifiée

- Le PNAF togolais (Décret n°2026-037/PC, 15 avril 2026) attribue et
  coordonne les bandes radioélectriques, y compris plusieurs sous-bandes
  à 5 GHz, mais ne confère aucune exemption générale de décodage à un
  particulier. (Confiance élevée)
- L'article 89 du droit togolais des communications électroniques
  sanctionne l'interception volontaire d'une communication privée par un
  dispositif électromagnétique. (Confiance moyenne — source relayée par
  l'UNODC, non le texte officiel direct)
- Aucune source trouvée ne crée d'exception explicite pour une équipe
  étudiante. Le scénario le plus prudent : mesurer une occupation de
  spectre (présence/signature) sans jamais décoder de contenu — ce qui
  correspond exactement à l'architecture déjà retenue pour VIGIE.
- L'harmonisation UEMOA/CEDEAO du spectre (rapport UIT) n'est pas une
  permission régionale d'interception.
- L'Acte additionnel CEDEAO A/SA.1/01/10 sur les données personnelles
  s'applique si le système enregistre des identifiants ou adresses MAC —
  à garder en tête si la portée du capteur s'étend.

**Action avant tout test terrain (pas avant le 30 septembre)** :
solliciter une confirmation écrite de l'ARCEP Togo ou un conseil
juridique local. Ne pas attendre cette confirmation pour le dépôt du
31 août — le concept et le prototype logiciel n'en dépendent pas.

## Limite à assumer explicitement dans le dossier

Un drone en vol totalement autonome, sans liaison radio active, reste
invisible à ce système. Documentée, non dissimulée.

## Sources

- ARCEP Togo — réglementation communications électroniques
- PNAF Togo 2026 (Décret n°2026-037/PC)
- UNODC — Loi togolaise sur les communications électroniques, art. 89
- UIT — Gestion du spectre UEMOA-CEDEAO
- ARCEP Burkina — Acte additionnel CEDEAO A/SA.1/01/10
- RTL-SDR Blog — datasheet V4
- Fiches produits Ubuy Togo, AliExpress, eBay, RTL-SDR Blog (consultées 17/08/2026)

Recherche menée via Manus, vérifiée et reformulée par Claude avant
intégration au repo.
