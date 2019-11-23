# Enhanced Aria #

* Autor: Jose Manuel Delicado
* NVDA compatibility: 2017.4 to 2019.2
* Preuzmi [stabilnu verziju][1]

Ovaj dodatak vam dozvoljava da odredite koji Aria orjentiri se prijavljuju
dok se pretražuje Web koristeći NVDA

Njegova funkcija je veoma jednostavna. Kada je instaliran, otvorite vaš Web
pretraživač i pretražujte kao i obično. Podrazumevani orjentiri koji se
prijavljuju u Firefoxu i Chromeu će takođe biti vidljivi u Internet
exploreru, tako da možete koristiti tastere brze navigacije da skočite do
njih, i listati ih komandom NVDA+f7 u svim pretraživačima. Pročitajte NVDA
korisničko uputstvo za više informacija.

Dodatak dodaje dodatni orjentir koji nije uključen u NVDA, članak (skraćeno
na brajevom redu kao art).

## Dijalog podešavanja

Možete onemogućiti i omogućiti orjentire iz NVDA menija, podešavanja,
Enhanced Aria podešavanja ili iz odgovarajuće kategorije NVDA dijaloga za
podešavanja. Dijalog ima izborno polje za svaki orjentir. Ako onemogućite
orjentir, nećete moći da skočite na njega tasterom d kada pretražujete Web
stranicu, i NVDA ga neće prijaviti.

## Kontakt informacije

Ovaj dodatak je napravljen od strane autora Jose Manuel Delicado. Ako želite
da ga kontaktirate, pošaljite e-mail na adresu jm.delicado@nvda.es, ili
prijavite grešku na Githubu na adresi
https://github.com/jmdaweb/enhancedAria

## Promene

### Version 2.7

* Ažurirani parametri kompatibilnosti za najnovije NVDA verzije.
* Novi i ažurirani prevodi.

### Version 2.6

* Updated compatibility flags for recent NVDA versions. This version is only
  compatible with NVDA 2017.4 and above.
* Novi i ažurirani prevodi.
* Now, the configuration is automatically applied after switching NVDA
  profiles and restoring settings to factory defaults.

### Verzija 2.5

* Ažurirani parametri kompatibilnosti za najnovije NVDA verzije.

### Verzija 2.4

* Sada, podešavanja se uklanjaju samo kada se dodatak ukloni. Podešavanja
  više neće biti resetovana nakon ažuriranja.
* Novi i ažurirani prevodi.

### Verzija 2.3

* Dodata kompatibilnost sa najnovijim NVDA verzijama.
* Novi prevodi.

### Verzija 2.2

* Ispravljena velika greška kada se koristi brajev red uz podešeno
  prijavljivanje članaka.

### Verzija 2.1

* Poboljšanja stabilnosti

### Verzija 2.0

* Dodata podrška za dijaloge kategorija podešavanja dostupni u NVDA verziji
  2018.2 i novijim.
* Dodata kompatibilnost za Python 3
* Sada se koristi guiHelper modul za pravljenje interfejsa dodatka.

### Verzija 1.3

* Dodata configobj specifikacija za podešavanja dodatka

### Verzija 1.2

* Greške ispravljene

### Verzija 1.1

* Popravljeni problemi u otvaranju dijaloga za podešavanje dodatka kada se
  NVDA vrati na sačuvana podešavanja

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
