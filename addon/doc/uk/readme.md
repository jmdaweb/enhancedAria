# Enhanced Aria #

* Автор: Jose Manuel Delicado
* Legacy add-on: NVDA 2019.3 and later can read articles on the web
* NVDA compatibility: 2017.4 to 2019.2
* Завантажити [стабільну версію][1]

Цей додаток дозволяє вам обрати, які орієнтири на WEB-сторінках має
промовляти NVDA.

Його функціонал дуже простий. Після встановлення відкрийте браузер і
заходьте до інтернету, як зазвичай. Типові орієнтири, які озвучуються у
Firefox і Chrome, також будуть видимими в Internet Explorer, тому ви зможете
натискати клавіші швидкої навігації для переміщення між ними, і переглянути
список усіх орієнтирів на сторінці після натискання NVDA+F7 у всіх
браузерах. Прочитайте посібник користувача NVDA для отримання додаткової
інформації.

The addon adds an extra landmark not included by default in NVDA, the
article (abbreviated in Braille as art).

## Діалог налаштувань

You can enable or disable landmarks by going to NVDA, preferences, Enhanced
Aria Settings or from the appropriate category in the NVDA options
dialog. The dialog has a checkbox for each landmark. If you disable a
landmark, you won't be able to jump to it pressing the d key when browsing a
webpage, and NVDA won't report it.

## Контактна інформація

This addon has been developed by Jose Manuel Delicado. If you want to
contact me, send an e-mail to jm.delicado@nvda.es, or open an issue on
GitHub at https://github.com/jmdaweb/enhancedAria

## Журнал змін

### Version 2.8

* New and updated translations.
* Updated NVDA compatibility flags.

### Version 2.7

* Updated compatibility flags for recent NVDA versions.
* New and updated translations.

### Version 2.6

* Updated compatibility flags for recent NVDA versions. This version is only
  compatible with NVDA 2017.4 and above.
* New and updated translations.
* Now, the configuration is automatically applied after switching NVDA
  profiles and restoring settings to factory defaults.

### Version 2.5

* Updated compatibility flags for recent NVDA versions.

### Version 2.4

* Now, settings are removed only when the add-on is
  uninstalled. Configuration is nolonger reset when upgrading.
* New and updated translations.

### Version 2.3

* Added compatibility with recent NVDA releases.
* New translations.

### Version 2.2

* Fixed a fatal error when a Braille display was used and the article role
  was configured to be reported.

### Version 2.1

* Stability improvements

### Версія 2.0

* Додано підтримку багатосторінкового діалогу з категоріями налаштувань
  NVDA, який доступний в NVDA 2018.2 і новіших версіях
* Added Python 3 compatibility
* Now guiHelper module is used to create the addon interface

### Версія 1.3

* Added configobj specification for addon settings

### Версія 1.2

* Bugs fixed

### Версія 1.1

* Fixed issues which prevented opening the addon settings dialog when
  reverting to NVDA saved configuration

[[!tag dev stable legacy]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
