# Enhanced Aria #

* Autor: Jose Manuel Delicado
* NVDA compatibility: 2017.3 to 2019.1
* Preuzmi [stable version][1]

Ovaj dodatak dozvoljava vam da odredite koji Aria orijentiri se prijavljuju
dok pretražujete Internet.

Njegova funkcija je vrlo jednostavna. Kada je instaliran, otvorite vaš Web
preglednik i pretražujte kao i obično. Podrazumijevani orijentiri koji se
prijavljuju u Firefoxu i Chromeu će također biti vidljivi u Internet
Exploreru, tako da možete koristiti tipke brze navigacije da skočite i
skočite do njih komandom NVDA+F7 u svim pretraživačima.

The addon adds an extra landmark not included by default in NVDA, the
article (abbreviated in Braille as art).

## Dijaloški okvir konfiguracije 

You can enable or disable landmarks by going to NVDA, preferences, Enhanced
Aria Settings or from the appropriate category in the NVDA options
dialog. The dialog has a checkbox for each landmark. If you disable a
landmark, you won't be able to jump to it pressing the d key when browsing a
webpage, and NVDA won't report it.

## Kontakt informacije

This addon has been developed by Jose Manuel Delicado. If you want to
contact me, send an e-mail to jm.delicado@nvda.es, or open an issue on
GitHub at https://github.com/jmdaweb/enhancedAria

## Promjene

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

### Version 2.0

* Added support for multi-category settings dialog available on NVDA 2018.2
  and later
* Added Python 3 compatibility
* Now guiHelper module is used to create the addon interface

### Version 1.3

* Dodana configobj specifikacija za postavke dodatka

### Inačica 1.2

* Ispravljene greške

### Inačica 1.1

* Popravljeni problemi u otvaranju dijaloškog okvira za podešavanje dodatka
  kada se NVDA vrati na spremljene postavke

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
