# Poboljšana ARIA svojstva (Enhanced Aria) #

* Autor: Jose Manuel Delicado
* NVDA kompatibilnost: 2017.4 do 2019.2
* Preuzmi [stabilnu verziju][1]

Ovaj dodatak dozvoljava određivanje ARIA orijentira o kojima se izvještava
za vrijeme čitanja u internetu.

Njegova funkcija je vrlo jednostavna. Kad je dodatak instaliran, otvori Web
preglednik i pretraži kao i obično. Standardni ARIA orijentiri koji se
prijavljuju u Firefoxu i Chromeu će također biti vidljivi u Internet
Exploreru, tako da je moguće koristiti tipke brze navigacije za prelaženje
između pojedinih orijentira i izraditi popis orijentira pomoću tipkovnog
prečaca NVDA+F7 u svim pretraživačima. Korisnički vodič za NVDA sadrži
daljnje informacije.

Dodatak dodaje dodatni orijentir koji nije standardno uključen u NVDA, a to
je članak.

## Dijaloški okvir konfiguracije

Orijentiri se mogu aktivirati ili deaktivirati putem NVDA>Postavke>Postavke
za poboljšana ARIA svojstva ili putem odgovarajuće kategorije u dijaloškom
okviru za mogućnosti. U dijaloškom okviru se nalazi potvrdni okvir za svaki
orijentir. Ako se orijentir deaktivira, prilikom čitanja web stranica neće
biti moguće skočiti na njega pritiskom tipke „d”, a NVDA o tome neće
izvjestiti.

## Kontakt informacije

Razvijatelj ovog dodatka je Jose Manuel Delicado. Ako me želiš kontaktirati,
pošalji e-mail na jmdaweb@hotmail.com ili prijavi grešku na GitHubu na
adresi https://github.com/jmdaweb/enhancedAria

## Promjene

### Verzija 2.7

* Aktualizirane su kompatibilne oznake za novije NVDA verzije.
* Novi i aktualizirani prijevodi.

### Verzija 2.6

* Aktualizirane su kompatibilne oznake za nedavne NVDA verzije. Ova je
  verzija kompatibilna samo s NVDA 2017.4 i novijim verzijama.
* Novi i aktualizirani prijevodi.
* Konfiguracija se sada automatski primjenjuje nakon prebacivanja NVDA
  profila i vraćanja postavki na tvornički zadane postavke.

### Verzija 2.5

* Aktualizirane su kompatibilne oznake za novije NVDA verzije.

### Verzija 2.4

* Postavke se sada uklanjaju samo kad je dodatak deinstaliran. Konfiguracija
  se više ne resetira prilikom nadogradnje.
* Novi i aktualizirani prijevodi.

### Verzija 2.3

* Dodana kompatibilnost s novijim NVDA izdanjima.
* Novi prijevodi.

### Verzija 2.2

* Ispravljena je fatalna greška tijekom upotrebe brajičnog retka i uloga
  članka je konfigurirana za izvještavanje.

### Verzija 2.1

* Poboljšana stabilnost

### Verzija 2.0

* Dodana je podrška za dijaloški okvir postavaka višestrukih kategorija, što
  je dostupno u NVDA 2018.2 i novijim izdanjem
* Dodana je Python 3 kompatibilnost
* Sada se koristi „guiHelper” modul za izradu sučelja dodatka

### Verzija 1.3

* Dodana configobj specifikacija za postavke dodatka

### Verzija 1.2

* Ispravljene greške

### Verzija 1.1

* Popravljeni su problemi prilikom otvaranja dijaloškog okvira za postavke
  dodatka, kad se NVDA vrati na spremljene konfiguraciju

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
