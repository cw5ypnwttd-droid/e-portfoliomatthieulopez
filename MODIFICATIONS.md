# Modifier mon portfolio

Ouvrez contenu.js sur GitHub, cliquez sur le crayon et modifiez les valeurs entre guillemets. Conservez les virgules et les guillemets, puis cliquez sur « Commit changes ».

- Présentation : profil > presentation.
- Coordonnées : profil > email, telephone et linkedin.
- Photo : importez photo.jpg dans assets/photo/, puis mettez assets/photo/photo.jpg dans profil > photo. La photo du CV n’est pas utilisée comme portrait sur le site.
- CV : intégré dans assets/cv/cv-matthieu-lopez.pdf. Pour le remplacer, importez le nouveau PDF sous le même nom.
- TIPE : 45 images dans assets/projets/diapos/ pour le défilement et un PDF dans assets/projets/tipe-coraux.pdf.
- Vidéo : renseignez video > source et type (youtube, vimeo ou locale).

Pour publier cette version, décompressez le ZIP et importez son contenu dans votre dépôt GitHub en conservant les dossiers. Les 45 images de diapositives doivent être importées aussi.

Le CV est désormais affiché via assets/cv/cv-apercu.png pour être visible aussi sur mobile et en ouverture locale. Si vous changez le PDF, remplacez également cette image par un aperçu du nouveau CV.

## Version anglaise
Les textes français restent dans contenu.js. Les textes anglais sont dans contenu-en.js. Le portrait et les coordonnées sont partagés depuis contenu.js. Les boutons FR / EN conservent la page courante et enregistrent la langue. Les liens ?lang=en et ?lang=fr permettent de choisir la langue directement.
Le CV anglais est assets/cv/cv-matthieu-lopez-en.pdf et son aperçu assets/cv/cv-apercu-en.png. Les diapositives originales du TIPE restent en français ; le texte de présentation du projet est traduit.
Importez aussi contenu-en.js, i18n.js et les nouveaux fichiers du dossier assets/cv/ sur GitHub.

## Version à six rubriques
Les engagements civiques et les activités sont modifiables dans engagements et interets, dans les deux fichiers de contenu. Les cartes HVSS s’ouvrent en cliquant sur « Pourquoi je m’engage » et « Le déclic ». La carte de mobilité et les photographies fonctionnent sans service de carte externe. Choisir Monde ou Europe pour changer la vue.

Pour mettre à jour GitHub, importer aussi rubriques.js et tout le dossier assets/mobilite. Importer moins de 100 fichiers par envoi : si GitHub refuse l’ensemble, envoyer les fichiers de la racine et .github, puis le dossier assets dans un deuxième envoi. Conserver les noms et les sous-dossiers.

## Version 7
Lagos (Portugal) et Porto sont ajoutés à la carte (17 villes). Les engagements et activités utilisent des cases à ouvrir en cliquant sur leur titre. Le parcours alterne de part et d’autre d’une ligne centrale sur ordinateur et reste sur une colonne sur téléphone. Le prénom est affiché dans l’en-tête.

## Version 8
Engagements complétés : formations HVSS par 7fe Space, parcours de don de sang puis de plasma, Clean Walk avec le BDD à Toulouse. Expérience de ripeur à la mairie de Sartrouville ajoutée pour août 2026. Les PDF des CV restent les documents précédemment fournis.

## Version 12
Navigation persistante sur toutes les pages. Mobilité : 20 villes, dont Santander. Récits français et anglais ajoutés pour Boston, New York, Bilbao, Santander, Palerme, Glasgow, Dublin et Galway. Photos personnelles à Galway et Glasgow. Deux flèches permettent de consulter les deux images de Galway. Les récits sont modifiables dans les champs texteFr/texteEn des villes dans rubriques.js.

## Version 13
Lagos et Porto : récits des tournois et photos de handball, également disponibles en ouvrant la case Handball. Porto conserve son image de ville. Munich : deux photos personnelles, voyage scolaire et mention des JO de 1972. Tous les récits sont traduits en anglais.

## Version 14
Photos personnelles intégrées à Boston, New York (galerie de deux photos) et Dublin. L’engagement HVSS est désormais intitulé Formation HVSS / HVSS Training et décrit des formations suivies pour devenir staffeur, sans affirmer que ce rôle est déjà exercé.

## Version 15
Photos de Grenade, Amsterdam, Turin et Genève intégrées ; fichiers HEIC convertis en JPEG. Récits français et anglais ajoutés pour Grenade, Amsterdam et Turin. Saint-Sébastien et Bruxelles retirées : 18 villes restent sur la carte. Genève conserve son texte en attente de précisions.

## Version 16
Portrait légèrement retouché intégré à l’accueil et à l’en-tête sur toutes les pages, ainsi qu’aux CV français et anglais. Les deux aperçus de CV sont régénérés et les PDF téléchargeables mis à jour. Le contenu des CV est conservé. Pour changer le portrait du site, remplacer assets/photo/matthieu-lopez.png. Les PDF doivent être modifiés séparément.

## Version 17
Cadrage des portraits des deux CV corrigé : plus large, sans étirement, intégré à la mise en page avec des coins légèrement arrondis. Aperçus et téléchargements du site mis à jour.

## Version 18
Texte sur le violon étoffé (découverte en CP, concerts, auditions, gestion du trac et musique classique). Récits Paris et Genève ajoutés ; visite du siège de l’ONU à New York précisée. Textes mis à jour en français et anglais.

## Version 19
Mes destinations d’échange : trois souhaits (KAIST, Strathclyde, Université technique tchèque), textes dans echanges dans contenu.js et contenu-en.js. Cette rubrique est à côté de la vidéo sur ordinateur et en dessous sur mobile. La liste des trois ingénieurs est dans ingenieurs. Le changement de langue mémorise la rubrique et une position relative dans celle-ci, puis restaure le défilement après chargement.

## Version finale 20
Vidéo de présentation intégrée à côté des destinations d’échange. Lecture directe avec commandes, format vertical conservé et couverture. Fichier optimisé sous 25 Mo pour l’importation web sur GitHub. Lire MISE-EN-LIGNE-FINALE.md pour publier.
