# Site public VIGIE

Page unique, autonome, déployée sur Cloudflare Pages.

## Contenu

| Fichier | Rôle |
|---|---|
| `index.html` | La page complète — images et styles intégrés, aucune dépendance externe sauf les polices Google |
| `fiche_vigie.pdf` | La fiche de candidature, accessible en téléchargement direct depuis le site |

## Déploiement Cloudflare (connecté à ce dépôt)

Une fois configuré via Git, **chaque push sur `main` redéploie le site automatiquement.**

> ⚠️ Cloudflare a retiré l'option de création "Pages" du bouton
> "Create application" — tout passe désormais par "Workers", qui
> supporte aussi la connexion Git et le redéploiement automatique. Le
> point qui compte n'est donc plus "Workers vs Pages", mais de bien
> choisir **"Import a repository"** à l'étape 2 (pas un template, pas
> "Hello World") — c'est cette option précise qui active le
> redéploiement automatique par push.
>
> Contrairement à l'ancien Pages, un Worker a besoin d'un petit
> fichier de configuration pour savoir quoi déployer : c'est
> [`wrangler.jsonc`](../wrangler.jsonc), déjà présent à la racine du
> dépôt. Il pointe vers `./site` comme dossier de fichiers statiques —
> rien à modifier, il est prêt.

1. Sur `dash.cloudflare.com` → **Workers & Pages** → **Create application**.
2. Repérer l'option **"Import a repository"** et cliquer sur son
   bouton **"Get started"**.
3. Choisir GitHub, autoriser l'accès si demandé, sélectionner le dépôt
   **VIGIE**.
4. Configuration du projet :
   - **Build command** : laisser vide (aucune compilation nécessaire)
   - **Deploy command** : laisser la valeur par défaut,
     `npx wrangler deploy` — c'est elle qui lit `wrangler.jsonc` et
     déploie le contenu de `site/`
   - **Root directory** : laisser à la racine du dépôt (ne pas mettre
     `site` ici — c'est `wrangler.jsonc` qui s'en charge)
5. **Save and Deploy**. L'URL générée est en `.workers.dev` — c'est
   normal, ce n'est plus le signe d'un problème.
6. Vérifier que la section "Ce que nous traçons" (les 6 dimensions)
   apparaît bien sur le site déployé — c'est la partie la plus
   récente ; si elle manque, le déploiement n'a pas pris le dernier
   commit.
7. L'auto-déploiement se vérifie ensuite dans **Settings > Builds** du
   Worker sur le dashboard.

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
