# Enhanced Aria #

* Autor: Jose Manuel Delicado
* NVDA compatibility: 2017.3 to 2019.1
* Preuzmi [stabilnu verziju][1]

Ovaj dodatak vam dozvoljava da odredite koji Aria orjentiri se prijavljuju
dok se pretražuje Web koristeći NVDA

Njegova funkcija je veoma jednostavna. Kada je instaliran, otvorite vaš Web
pretraživač i pretražujte kao i obično. Podrazumevani orjentiri koji se
prijavljuju u Firefoxu i Chromeu će takođe biti vidljivi u Internet
exploreru, tako da možete koristiti tastere brze navigacije da skočite do
njih, i listati ih komandom NVDA+f7 u svim pretraživačima. Pročitajte NVDA
korisničko uputstvo za više informacija.

The addon adds an extra landmark not included by default in NVDA, the
article (abbreviated in Braille as art).

## Dijalog podešavanja

You can enable or disable landmarks by going to NVDA, preferences, Enhanced
Aria Settings or from the appropriate category in the NVDA options
dialog. The dialog has a checkbox for each landmark. If you disable a
landmark, you won't be able to jump to it pressing the d key when browsing a
webpage, and NVDA won't report it.

## Kontakt informacije

This addon has been developed by Jose Manuel Delicado. If you want to
contact me, send an e-mail to jm.delicado@nvda.es, or open an issue on
GitHub at https://github.com/jmdaweb/enhancedAria

## Promene

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

* Added configobj specification for addon settings

### Verzija 1.2

* Greške ispravljene

### Verzija 1.1

* Popravljeni problemi u otvaranju dijaloga za podešavanje dodatka kada se
  NVDA vrati na sačuvana podešavanja

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
