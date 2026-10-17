# Mon e-portfolio

Un modèle en français, léger, responsive et sans service externe obligatoire. Aucun serveur applicatif, aucune base de données et aucune installation de dépendances. Les contenus proposés sont des **exemples**, pas votre parcours réel.

## 1. Prévisualiser

Décompressez l’archive. Ouvrez `index.html` dans votre navigateur pour découvrir la page. Les modifications s’affichent après enregistrement et actualisation. L’aperçu PDF et la copie automatique de l’e-mail nécessitent parfois une prévisualisation HTTP : si ces fonctions ne sont pas disponibles en ouverture directe, essayez la version GitHub Pages.

Pour une prévisualisation locale complète : ouvrez le dossier dans Visual Studio Code, installez l’extension **Live Server**, faites un clic droit sur `index.html`, puis **Open with Live Server**. Autre possibilité, si Python est installé : ouvrez un terminal dans ce dossier et lancez `python3 -m http.server 8000`, puis consultez http://localhost:8000. Arrêtez avec Ctrl+C.

## 2. Un seul fichier pour les contenus

Ouvrez **contenu.js** dans un éditeur de texte brut (Visual Studio Code, par exemple). Chaque champ comporte un nom et une valeur. Modifiez les valeurs entre guillemets, gardez les virgules et accolades. Ne supprimez pas `window.CONTENU =` ni le point-virgule final. Pour écrire un guillemet dans une valeur, utilisez `\"`. Un champ facultatif vide s’écrit `""`.

| Rubrique dans contenu.js | Ce que vous pouvez modifier |
| --- | --- |
| `profil` | Nom, titre, courte présentation, photo, e-mail, LinkedIn |
| `parcours` | Expériences et formations |
| `projets` | Cartes, catégories, images, détails et liens |
| `cv` | Chemin du PDF et texte d’introduction |
| `video` | Titre, texte, fichier ou lien, couverture, sous-titres |
| `contact` | Titre et invitation à échanger |

Les intitulés de navigation sont dans `index.html` et `cv.html`. La palette est au début de `style.css` (`--ink`, `--paper`, `--lime`). Les exemples de projets utilisent des illustrations SVG locales que vous pouvez conserver ou remplacer.

## 3. Nom, photo et présentation

Dans `profil`, remplacez `[PRÉNOM NOM]`, `[TITRE OU FORMATION]` et le texte de `presentation`. Placez votre photo dans **assets/photo/**, par exemple `portrait.jpg`, puis indiquez `"photo": "assets/photo/portrait.jpg"`. Renseignez `photoAlternative` avec une description brève. Un portrait vertical est conseillé. Si `photo` reste vide, le site conserve une silhouette soignée.

## 4. Ajouter ou supprimer une expérience

Dans `parcours`, copiez un bloc complet de `{` à `}` et séparez les blocs par une virgule. Supprimez un bloc pour retirer une expérience. Voici un exemple de bloc :

```json
{
  "dateTri": "2026-09",
  "periode": "Septembre 2026 — Aujourd’hui",
  "intitule": "Votre poste ou votre formation",
  "structure": "Votre entreprise ou établissement",
  "description": "Vos missions et vos apprentissages.",
  "competences": ["Organisation", "Communication"],
  "exemple": false
}
```

`dateTri` doit respecter **AAAA-MM** : c’est la date de début utilisée pour le classement décroissant. Pour une expérience en cours, utilisez sa date de début et écrivez « Aujourd’hui » dans `periode`. L’ordre des blocs dans le fichier n’a pas d’importance. Passez `exemple` à `false` lorsque le texte décrit votre parcours réel. Vous pouvez aussi vider la liste : `"parcours": []`. Retirez alors la note de démonstration dans `index.html` si elle n’est plus pertinente.

## 5. Ajouter un projet

Dupliquez un bloc dans `projets`, avec une virgule entre les blocs. Renseignez `titre`, `categorie`, `description`, `competences`, puis les cinq textes `contexte`, `objectif`, `role`, `realisations`, `resultats`. Les filtres se créent automatiquement à partir des catégories ; utilisez une orthographe identique pour regrouper plusieurs projets.

Placez une image dans **assets/projets/** et renseignez par exemple `"image": "assets/projets/mon-projet.jpg"`. Une image horizontale est conseillée. Si le champ est vide ou le fichier absent, une zone de remplacement s’affiche.

Les champs `demo`, `document` et `github` sont facultatifs : utilisez une adresse complète `https://…` ou un chemin de document local. **Un champ vide masque son bouton.** Passez `exemple` à `false` pour une réalisation réelle. Pour supprimer un projet, retirez son bloc. `"projets": []` affiche un message d’attente.

## 6. Ajouter le CV

Copiez un véritable PDF dans **assets/cv/**, par exemple `mon-cv.pdf`. Dans `cv`, indiquez `"fichier": "assets/cv/mon-cv.pdf"`. La page `cv.html` affiche alors un aperçu, un bouton d’ouverture et un téléchargement. Le navigateur peut utiliser son propre lecteur ; sur mobile, le bouton d’ouverture reste disponible. Le téléchargement dépend des réglages du navigateur.

Si `fichier` est vide, un message d’attente apparaît. Un fichier absent ou qui n’est pas un PDF déclenche un message explicite, sans aperçu cassé. Après chaque remplacement, vérifiez le PDF sur la version publiée.

## 7. Ajouter la vidéo

Choisissez une des trois possibilités dans `video` :

- Fichier local : `"type": "locale"`, `"source": "assets/video/presentation.mp4"`.
- YouTube : `"type": "youtube"`, `"source": "https://www.youtube.com/watch?v=IDENTIFIANT"` (ou un lien youtu.be).
- Vimeo : `"type": "vimeo"`, `"source": "https://vimeo.com/IDENTIFIANT"`.

Pour une vidéo locale, copiez le fichier dans **assets/video/**. MP4 avec codecs H.264/AAC est largement compatible. Ajoutez une image locale dans `couverture`, par exemple `assets/video/couverture.jpg`, et un fichier WebVTT français dans `sousTitres`, par exemple `assets/video/sous-titres.vtt`. Ces deux champs sont facultatifs ; les sous-titres améliorent l’accessibilité. Exemple de fichier `.vtt` :

```text
WEBVTT

00:00:00.000 --> 00:00:04.000
Bonjour, bienvenue dans mon portfolio.
```

Pour YouTube/Vimeo, configurez la couverture et les sous-titres sur la plateforme vidéo : le lecteur utilise leurs réglages. L’intégration doit être autorisée par la plateforme et le propriétaire. Aucun lecteur ne démarre automatiquement. Sans source, un emplacement de démonstration est affiché ; une couverture locale peut l’illustrer.

Évitez les gros fichiers : GitHub limite les fichiers ordinaires à 100 Mio. Pour une vidéo lourde, préférez YouTube ou Vimeo.

## 8. E-mail et LinkedIn

Dans `profil`, remplacez `"email": ""` par votre adresse, par exemple `"email": "prenom@example.com"`. Le site propose le lien « M’envoyer un e-mail » (qui ouvre la messagerie du visiteur) et un bouton de copie. La copie automatique nécessite généralement HTTPS, fourni par GitHub Pages. Si le navigateur refuse, l’adresse reste sélectionnable. Sans adresse valide, aucun faux lien n’est créé.

Remplacez `"linkedin": ""` par l’URL complète de votre profil, par exemple `https://www.linkedin.com/in/votre-identifiant/`. Le bouton est masqué tant que ce champ est vide. Il n’y a pas de formulaire d’envoi ni de secret à configurer. Toute information publiée dans ce site est publique.

## 9. Publier sur GitHub Pages

1. Connectez-vous à GitHub et créez un dépôt vide, par exemple **mon-portfolio**. Pour un compte gratuit, choisissez un dépôt public.
2. Envoyez **le contenu du dossier e-portfolio**, pas son dossier parent : `index.html` doit être à la racine du dépôt. Utilisez **Add file → Upload files**, ou GitHub Desktop pour ajouter le dossier entier. Veillez à inclure le dossier caché **.github/workflows/** et le fichier `.nojekyll` ; sur Mac, Cmd+Maj+. affiche les fichiers cachés. Si l’interface web les omet, utilisez **Add file → Create new file**, donnez le chemin `.github/workflows/pages.yml` et collez son contenu.
3. Vérifiez que la branche s’appelle **main**. Le workflow fourni attend cette branche.
4. Dans **Settings → Pages → Build and deployment → Source**, choisissez **GitHub Actions**.
5. Ouvrez **Actions → Publier le portfolio sur GitHub Pages**. Si nécessaire, cliquez sur **Run workflow**. Les modifications suivantes de `main` republient automatiquement le site.
6. Une fois le déploiement vert, GitHub affiche l’adresse dans **Settings → Pages**. Pour un dépôt classique : `https://VOTRE-COMPTE.github.io/mon-portfolio/`.

Si le dépôt s’appelle `VOTRE-COMPTE.github.io`, le site est servi directement à la racine du domaine. Les deux configurations fonctionnent : tous les chemins internes sont relatifs. Respectez les minuscules/majuscules et privilégiez des noms de fichiers sans espace ni accent. Ne commencez pas les chemins de vos médias par `/`.

GitHub Desktop peut être plus pratique pour envoyer toutes les modifications : ouvrez le dossier comme dépôt local, créez un commit puis **Publish repository**. Aucun accès GitHub ni dépôt n’était connecté pendant la création : cette livraison est locale, elle n’est pas encore publiée.

## 10. Vérifier après personnalisation

Consultez l’accueil et le CV sur téléphone et ordinateur. Essayez le menu, chaque filtre, une fiche projet, la fermeture avec Échap et la navigation avec Tab. Contrôlez les dates, vos liens, la copie de l’e-mail, le PDF et la vidéo. Les animations respectent le réglage système « Réduire les animations ». Les exemples et les champs entre crochets sont à remplacer avant de partager votre portfolio.

## Fichiers

`index.html` : accueil et rubriques · `cv.html` : CV dédié · `contenu.js` : contenus · `style.css` : apparence · `app.js` : interactions · `assets/` : médias · `.github/workflows/pages.yml` : publication automatique.
