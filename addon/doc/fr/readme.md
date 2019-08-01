# Enhanced Aria #

* Auteur : Jose Manuel Delicado
* NVDA compatibility: 2017.4 to 2019.2
* Télécharger [version stable][1]

Cette extension vous permet de choisir quelles régions aria doivent être
signalées par NVDA lorsque vous naviguez sur Internet.

Sa fonctionnalité est très simple. Une fois installée, ouvrez votre
navigateur Web et visitez le Web comme d'habitude. Les régions aria par
défaut signalées par Firefox et Chrome seront également visibles dans
Internet Explorer, afin que vous puissiez appuyer sur les touches de
navigation rapide pour passer entre elles et les répertorier en appuyant sur
NVDA + f7 dans tous les navigateurs. Veuillez consulter le Guide de
l'utilisateur NVDA pour plus d'informations.

L'extension ajoute une région supplémentaire non incluse par défaut dans
NVDA, l'article (abrégé en Braille comme art).

## Le dialogue de configuration

Vous pouvez activer ou désactiver les régions en  allant dans NVDA, puis
dans Préférences, puis dans Paramètres Enhanced Aria ou à partir de la
catégorie appropriée dans le dialogue des options de NVDA. Le dialogue
comporte une case à cocher pour chaque région. Si vous désactivez une
région, vous ne pourrez pas y accéder en appuyant sur la touche d lorsque
vous naviguez sur une page Web, et NVDA ne la signalera pas.

## Information de contact

Cette extension a été développée par Jose Manuel Delicado. Si vous souhaitez
me contacter, envoyez un e-mail à jm.delicado@nvda.es, ou ouvrez un incident
sur GitHub à l'adresse https://github.com/jmdaweb/enhancedAria

## Journal des changements

### Version 2.7

* Les indicateurs de compatibilité ont été mis à jour pour les versions
  récentes de NVDA.
* Nouvelles traductions et mises à jour.

### Version 2.6

* Updated compatibility flags for recent NVDA versions. This version is only
  compatible with NVDA 2017.4 and above.
* Nouvelles traductions et mises à jour.
* Now, the configuration is automatically applied after switching NVDA
  profiles and restoring settings to factory defaults.

### Version 2.5

* Les indicateurs de compatibilité ont été mis à jour pour les versions
  récentes de NVDA.

### Version 2.4

* Désormais, les paramètres ne sont supprimés que lorsque l'extension est
  désinstallé. La configuration n'est plus réinitialisée lors de la mise à
  niveau.
* Nouvelles traductions et mises à jour.

### Version 2.3

* Ajout de la compatibilité avec les dernières versions de NVDA.
* Nouvelles traductions.

### Version 2.2

* Correction d'une erreur fatale quand on utilise un Afficheur Braille et
  que le rôle de l'article a été configuré pour être signalé.

### Version 2.1

* Amélioration de la stabilité

### Version 2.0

* Ajout de la prise en charge du dialogue des paramètres multi-catégories
  disponible sur NVDA 2018.2 et versions ultérieures
* Ajout de la compatibilité Python 3
* Maintenant, le module guiHelper est utilisé pour créer l'interface de
  l'extension

### Version 1.3

* Ajout de la spécification configobj pour les paramètres de l'extension

### Version 1.2

* Bugs corrigés

### Version 1.1

* Correction de problèmes qui empêchaient d'ouvrir le dialogue des
  paramètres des extensions lors de la réintégration à la configuration
  sauvegardée de NVDA

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
