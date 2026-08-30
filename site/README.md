# Site public VIGIE

Page unique, autonome, déployée sur Cloudflare Pages.

## Contenu

| Fichier | Rôle |
|---|---|
| `index.html` | La page complète — images et styles intégrés, aucune dépendance externe sauf les polices Google |
| `fiche_vigie.pdf` | La fiche de candidature, accessible en téléchargement direct depuis le site |

## Déploiement Cloudflare Pages (connecté à ce dépôt)

Une fois configuré, **chaque push sur `main` redéploie le site automatiquement.**

> ⚠️ Cloudflare a fusionné les interfaces Workers et Pages sous un
> même menu "Workers & Pages". Bien choisir l'onglet **Pages** à
> l'étape 2 ci-dessous — le flux "Workers" produit une URL en
> `.workers.dev` sans le même redéploiement automatique par push que
> "Pages" (URL en `.pages.dev`).

1. Sur `dash.cloudflare.com` → **Workers & Pages** → **Create** (ou
   **Create application**).
2. Choisir l'onglet **Pages** (pas Workers) → **Connect to Git**.
3. Autoriser l'accès à GitHub si demandé, choisir le dépôt **VIGIE**,
   cliquer **Begin setup**.
4. Configuration du build :
   - **Framework preset** : `None`
   - **Build command** : laisser vide
   - **Build output directory** : `site`
5. **Save and Deploy**. Le site est publié sous `vigie-xxx.pages.dev`
   en une minute environ.
6. Vérifier que la section "Ce que nous traçons" (les 6 dimensions)
   apparaît bien sur le site déployé — c'est la partie la plus
   récente ; si elle manque, le déploiement n'a pas pris le dernier
   commit.
7. Optionnel : dans **Custom domains**, brancher un nom de domaine
   propre.

Aucune étape de compilation n'est nécessaire — le HTML est servi tel
quel.

## Modifier le site

Éditer `index.html`, committer, pousser. Cloudflare détecte le push et
redéploie seul. Pas d'upload manuel.

## Règle de contenu

Le site et la fiche PDF doivent rester cohérents entre eux et avec la
documentation du dépôt (`docs/`). Aucun chiffre de performance de
détection ne doit y figurer tant qu'aucune mesure réelle n'a été
produite — voir `docs/ethique.md` et `docs/contrat_evenement.md`.
