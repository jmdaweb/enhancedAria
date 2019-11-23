# Enhanced Aria #

* Autore: Jose Manuel Delicado
* Compatibilità con NVDA: dalla 2017.4 alla 2019.2
* Scarica la [versione stabile][1]

Questo componente aggiuntivo consente di personalizzare quali punti di
riferimento ARIA NVDA debba annunciare durante la navigazione web.

Le sue funzioni sono molto semplici. Una volta installato, aprire il browser
e navigare come al solito. Le sezioni mostrate in Google Chrome e Firefox
verranno mostrate anche in Internet Explorer; sarà possibile passare da una
all'altra come sempre con il tasto "d", e usare NVDA-f7 per visualizzarle
tutte in un elenco. Per maggiori informazioni su queste funzioni native di
NVDA consultare la documentazione.

Il componente aggiunge anche un nuovo tipo di punto di riferimento, chiamato
Articolo, (abbreviato in braille art).

## La finestra di configurazione

Puoi attivare o disattivare i punti di riferimento andando nel menu di NVDA,
preferenze, Enhanced Aria Settings, o dalle impostazioni di NVDA nella
relativa categoria. Nella finestra esiste una casella di controllo per
ciascun punto di riferimento. Se se ne disattiva uno di questi, non sarà più
possibile utilizzare il tasto "D" per raggiungerlo e NVDA non lo leggerà più
come tale.

## Informazioni di contatto

Questo componente è stato sviluppato da Jose Manuel Delicado. Per contatti è
possibile inviare un'email a jmdaweb@hotmail.com, o aprire una segnalazione
su GitHub su https://github.com/jmdaweb/enhancedAria

## Cambiamenti

### Versione 2.7

* Aggiunta la compatibilità con le recenti versioni di NVDA. 
* Traduzioni nuove e aggiornate

### Versione 2.6

* Aggiunta la compatibilità con le recenti versioni di NVDA. Questa versione
  risulta compatibile a partire da NVDA 2017.4 in poi
* Traduzioni nuove e aggiornate
* Ora, la configurazione viene automaticamente applicata dopo aver cambiato
  i profili NVDA e ripristinato le impostazioni predefinite di fabbrica.

### Versione 2.5

* Aggiunta la compatibilità con le recenti versioni di NVDA. 

### Versione 2.4

* Ora, le impostazioni vengono rimosse solo quando viene disinstallato il
  componente aggiuntivo. La configurazione non viene più ripristinata
  durante l'aggiornamento.
* Traduzioni nuove e aggiornate

### Versione 2.3

* Aggiunta la compatibilità con le recenti versioni di NVDA. 
* Nuove traduzioni. 

### Versione 2.2

* Fixed a fatal error when a Braille display was used and the article role
  was configured to be reported.

### Versione 2.1

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
