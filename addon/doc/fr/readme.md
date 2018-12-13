# Enhanced Aria #

* Auteur : Jose Manuel Delicado
* Compatibilité NVDA: 2017.3 à 2019.1
* Télécharger [version stable][1]

Ce module complémentaire vous permet de personnaliser les régions d'aria
signalés par NVDA lorsque vous naviguez sur Internet.

Sa fonctionnalité est très simple. Une fois installé, ouvrez votre
navigateur Web et visitez le Web comme d'habitude. Les régions par défaut
d'aria signalés par Firefox et Chrome seront également visibles dans
Internet Explorer, afin que vous puissiez appuyer sur les touches de
navigation rapide pour passer entre eux et les répertorier en appuyant sur
NVDA + f7 dans tous les navigateurs. Lisez le Guide de l'utilisateur NVDA
pour plus d'informations.

Le module complémentaire ajoute une région supplémentaire non inclus par
défaut dans NVDA, l'article (abrégé en Braille comme art).

## Le dialogue de configuration

Vous pouvez activer ou désactiver les régions en  allant dans NVDA, puis
dans Préférences, puis dans Paramètres Enhanced Aria ou à partir de la
catégorie appropriée dans le dialogue des options de NVDA. Le dialogue
comporte une case à cocher pour chaque région. Si vous désactivez une
région, vous ne pourrez pas y accéder en appuyant sur la touche d lorsque
vous naviguez sur une page Web, et NVDA ne le signale pas.

## Information de contact

Ce module complémentaire a été développé par Jose Manuel Delicado. Si vous
souhaitez me contacter, envoyez un e-mail à jm.delicado@nvda.es, ou ouvrez
une incidence sur GitHub à l'adresse https://github.com/jmdaweb/enhancedAria

## Journal des changements

### Version 2.3

* Ajout de la compatibilité avec les dernières versions de NVDA.
* Nouvelles traductions.

### Version 2.2

* Correction d'une erreur fatale lors de l'utilisation de l'Afficheur
  Braille et le rôle de l'article a été configuré pour être signalé.

### Version 2.1

* Amélioration de la stabilité

### Version 2.0

* Ajout de la prise en charge du dialogue des paramètres multi-catégories
  disponible sur NVDA 2018.2 et versions ultérieures
* Ajout de la compatibilité Python 3
* Maintenant, le module guiHelper est utilisé pour créer l'interface du
  module complémentaire

### Version 1.3

* Ajout de la spécification configobj pour les paramètres du module
  complémentaire

### Version 1.2

* Bugs corrigés

### Version 1.1

* Problèmes corrigés qui ont empêché d'ouvrir le dialogue des paramètres des
  modules complémentaires lors de la réintégration à la configuration
  sauvegardée de NVDA

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
