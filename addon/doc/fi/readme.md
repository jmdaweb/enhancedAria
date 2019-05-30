# Laajennettu Aria #

* Tekijä: Jose Manuel Delicado
* Yhteensopivuus: NVDA 2017.4-2019.2
* Lataa [vakaa versio][1]

Tämän lisäosan avulla voit mukauttaa, mitä ARIA-kiintopisteitä  NVDA puhuu
verkkosivuja selatessasi.

Toimintaperiaate on hyvin yksinkertainen. Kun lisäosa on asennettu, avaa
verkkoselain ja selaa haluamiasi sivuja tavalliseen tapaan. Firefoxin ja
Chromen ilmoittamat oletusarvoiset ARIA-kiintopisteet näkyvät myös Internet
Explorerissa, joten voit kaikissa selaimissa liikkua niiden välillä
pikanavigointikomennoilla sekä tuoda näkyviin luettelon niistä painamalla
NVDA+F7. Katso lisätietoja NVDA:n käyttöoppaasta.

NVDA:han lisätään artikkeli-kiintopiste (pistekirjoituksella lyhenteenä
"art"), jota ei oletuksena ole.

## Asetusvalintaikkuna

Voit ottaa kiintopisteitä käyttöön tai poistaa niitä käytöstä avaamalla
NVDA-valikon, valitsemalla Asetukset ja sieltä Laajennettu Aria tai
vastaavasta Asetusvalintaikkunan kategoriasta. Valintaikkunassa on kutakin
kiintopistettä varten oma valintaruutu. Jos poistat kiintopisteen käytöstä,
et voi enää verkkosivua selatessasi siirtyä siihen pikanavigointikomennolla
D, eikä NVDA myöskään puhu sitä.

## Yhteystiedot

Tämän lisäosan on kehittänyt Jose Manuel Delicado. Jos haluat ottaa yhteyttä
häneen, lähetä sähköpostia osoitteeseen jm.delicado@nvda.es tai avaa kysymys
GitHubissa osoitteessa https://github.com/jmdaweb/enhancedAria

## Muutosloki

### Versio 2.6

* Yhteensopivuusliput päivitetty uusimmille NVDA-versioille. Tämä versio on
  yhteensopiva vain NVDA 2017.4:n ja sitä uudempien kanssa.
* Uusia ja päivitettyjä käännöksiä.
* Asetukset otetaan nyt automaattisesti käyttöön, kun profiilia on vaihdettu
  ja asetukset palautettu oletusarvoihinsa.

### Versio 2.5

* Yhteensopivuusliput päivitetty uusimmille NVDA-versioille.

### Versio 2.4

* Asetukset poistetaan nyt vain, kun lisäosa poistetaan. Asetusten
  oletusarvoja ei palauteta päivitettäessä.
* Uusia ja päivitettyjä käännöksiä.

### Versio 2.3

* Lisätty yhteensopivuus viimeisimpien NVDA-versioiden kanssa.
* Uusia käännöksiä.

### Versio 2.2

* Korjattu vakava virhe, jota esiintyi pistenäyttöä käytettäessä ja kun
  artikkeli-rooli oli määritetty ilmoitettavaksi.

### Versio 2.1

* Vakautta parannettu.

### Versio 2.0

* Lisätty tuki NVDA 2018.2:n ja uudempien monikategoriaiselle
  asetusvalintaikkunalle
* Lisätty Python 3 -yhteensopivuus
* Lisäosan asetuskäyttöliittymän luomiseen käytetään nyt guiHelper-moduulia

### Versio 1.3

* Lisäosan asetukset noudattavat nyt configobj-moduulin määrityksiä.

### Versio 1.2

* Virheitä korjattu

### Versio 1.1

* Korjattu ongelmia, jotka estivät lisäosan asetusvalintaikkunan avaamisen
  palautettaessa NVDA:n tallennettuja asetuksia

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
