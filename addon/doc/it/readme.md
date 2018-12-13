# Enhanced Aria #

* Autore: Jose Manuel Delicado
* NVDA compatibility: 2017.3 to 2019.1
* Download [stable version][1]

Questo componente aggiuntivo consente di personalizzare quali sezioni, o
punti di riferimento,  ARIA NVDA debba annunciare durante la navigazione web

Le sue funzioni sono molto semplici. Una volta installato, aprire il browser
e navigare come al solito. Le sezioni mostrate in Google Chrome e Firefox
verranno mostrate anche in Internet Explorer; sarà possibile passare da una
all'altra come sempre con il tasto "d", e usare NVDA-f7 per visualizzarle
tutte in un elenco. Per maggiori informazioni su queste funzioni native di
NVDA consultare la documentazione.

The addon adds an extra landmark not included by default in NVDA, the
article (abbreviated in Braille as art).

## La finestra di configurazione

You can enable or disable landmarks by going to NVDA, preferences, Enhanced
Aria Settings or from the appropriate category in the NVDA options
dialog. The dialog has a checkbox for each landmark. If you disable a
landmark, you won't be able to jump to it pressing the d key when browsing a
webpage, and NVDA won't report it.

## Informazioni di contatto

This addon has been developed by Jose Manuel Delicado. If you want to
contact me, send an e-mail to jm.delicado@nvda.es, or open an issue on
GitHub at https://github.com/jmdaweb/enhancedAria

## Cambiamenti

### Version 2.3

* Added compatibility with recent NVDA releases.
* New translations.

### Version 2.2

* Fixed a fatal error when a Braille display was used and the article role
  was configured to be reported.

### Version 2.1

* Stability improvements

### Versione 2.0

* Aggiunto il supporto alle impostazioni multiCategoria disponibili da NVDA
  2018.2 e successive
* aggiunta compatibilità a Python 3
* Viene ora usato il modulo guiHelper per creare l'interfaccia utente del
  componente

### Versione 1.3

* Aggiunte specifiche configobj per le impostazioni del componente

### Versione 1.2

* Sistemati bug vari

### Versione 1.1

* Sistemato un bug che impediva l'apertura dell'interfaccia dell'addon, dopo
  che la configurazione di NVDA è stata ripristinata.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
