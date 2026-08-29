# Site public VIGIE

Page unique, autonome, déployée sur Cloudflare Pages.

## Contenu

| Fichier | Rôle |
|---|---|
| `index.html` | La page complète — images et styles intégrés, aucune dépendance externe sauf les polices Google |
| `fiche_vigie.pdf` | La fiche de candidature, accessible en téléchargement direct depuis le site |

## Déploiement Cloudflare Pages (connecté à ce dépôt)

Une fois configuré, **chaque push sur `main` redéploie le site automatiquement.**

1. Sur `dash.cloudflare.com` → **Workers & Pages** → **Create** → onglet **Pages** → **Connect to Git**.
2. Autoriser Cloudflare à accéder au compte GitHub, puis choisir le dépôt `VIGIE`.
3. Configuration du build :
   - **Framework preset** : `None`
   - **Build command** : laisser vide
   - **Build output directory** : `site`
4. **Save and Deploy**. Le site est publié sous `vigie-xxx.pages.dev` en une minute environ.
5. Optionnel : dans **Custom domains**, brancher un nom de domaine propre.

Aucune étape de compilation n'est nécessaire — le HTML est servi tel quel.

## Modifier le site

Éditer `index.html`, committer, pousser. Cloudflare détecte le push et
redéploie seul. Pas d'upload manuel.

## Règle de contenu

Le site et la fiche PDF doivent rester cohérents entre eux et avec la
documentation du dépôt (`docs/`). Aucun chiffre de performance de
détection ne doit y figurer tant qu'aucune mesure réelle n'a été
produite — voir `docs/ethique.md` et `docs/contrat_evenement.md`.
