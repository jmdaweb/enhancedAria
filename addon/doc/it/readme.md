# Enhanced Aria #

* Autore: Jose Manuel Delicado
* Add-on non più necessario. NVDA 2019.3 e le versioni successive sono in
  grado di leggere gli articoli nelle pagine web
* Compatibilità con NVDA: dalla versione 2017.4 alla 2019.2
* Scarica la [versione stabile][1]

Questo componente aggiuntivo consente di personalizzare quali punti di
riferimento ARIA NVDA debba annunciare quando si naviga in Internet.

Le sue funzioni sono molto semplici. Una volta installato, aprire il browser
e navigare come al solito. I landmark ARIA di default mostrati in Google
Chrome e Firefox verranno mostrate anche in Internet Explorer; sarà pertanto
possibile passare da una all'altra come sempre con i tasti di navigazione
veloce, e usare NVDA-f7 per visualizzarle tutte in un elenco. Per maggiori
informazioni su queste funzioni native di NVDA consultare il manuale
dell'utente.

Il componente aggiunge un nuovo tipo di punto di riferimento, non incluso in
NVDA, chiamato Articolo, (abbreviato in braille art).

## La finestra di configurazione

Puoi attivare o disattivare i punti di riferimento andando nel menu di NVDA
-> preferenze->  Enhanced Aria Settings, o dalle impostazioni di NVDA nella
relativa categoria. Nella finestra esiste una casella di controllo per
ciascun punto di riferimento. Se si disattiva uno di questi, non sarà
possibile utilizzare il tasto "D" per raggiungerlo quando si naviga in una
pagina web e NVDA non lo leggerà più come tale.

## Informazioni di contatto

Questo componente è stato sviluppato da Jose Manuel Delicado. Per contatti è
possibile inviare un'email a jmdaweb@hotmail.com, o aprire una segnalazione
su GitHub su https://github.com/jmdaweb/enhancedAria

## Cambiamenti

### Versione 2.8

* Traduzioni nuove e aggiornate
* Aggiunti i flag di compatibilità di NVDA.

### Versione 2.7

* Aggiunta la compatibilità con le recenti versioni di NVDA. 
* Traduzioni nuove e aggiornate

### Versione 2.6

* Aggiunta la compatibilità con le recenti versioni di NVDA. Questa versione
  è compatibile solo con NVDA 2017.4 o superiori.
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

* Corretto un errore critico che si verificava quando veniva utilizzato un
  display Braille e la lettura del ruolo "articolo" era attivata.

### Versione 2.1

* Miglioramenti alla stabilità 

### Versione 2.0

* Aggiunto il supporto per la finestra impostazioni multiCategoria,
  disponibile da NVDA 2018.2 e successive
* Aggiunta compatibilità con Python 3
* Viene ora usato il modulo guiHelper per creare l'interfaccia utente del
  componente

### Versione 1.3

* Aggiunte specifiche configobj per le impostazioni del componente

### Versione 1.2

* Corretti bug vari

### Versione 1.1

* Corretti bug che impedivano l'apertura della finestra impostazioni
  dell'addon, dopo che la configurazione di NVDA è stata ripristinata

[[!tag dev stable legacy]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
