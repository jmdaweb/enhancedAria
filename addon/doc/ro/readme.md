# Enhanced Aria #

* Autor: José Manuel Delicado
* Supliment tradițional: NVDA 2019.3 și mai nou poate citi articole pe web
* Compatibilitate NVDA: 2017.4 - 2019.2
* Descărcați [versiunea stabilă][1]

Acest supliment vă permite să particularizați ce repere sunt raportate de
NVDA când navigați pe Internet.

Funcționalitatea sa este foarte simplă. Odată instalat, deschideți
navigatorul dumneavoastră web și vizitați web-ul ca de obicei. Reperele aria
implicite raportate de Firefox și Chrome vor fi de asemenea vizibile în
Internet Explorer, așa că veți putea să apăsați tastele de navigare rapidă
pentru a sări printre ele și le puteți lista apăsând NVDA+f7 în toate
navigatoarele. Citiți ghidul de utilizare al NVDA-ului pentru mai multe
informații.

Suplimentul adaugă un reper suplimentar, care nu este inclus implicit în
NVDA, articolul (abreviat în braille ca art).

## Dialogul de configurare

Puteți activa sau dezactiva reperele mergând în meniul NVDA, preferințe,
setări Enhanced Aria. Dialogul are o casetă de bifat pentru fiecare
reper. Dacă dezactivați un reper, nu veți mai putea să săriți la el apăsând
tasta d la navigarea pe o pagină web, iar NVDA nu-l va mai raporta.

## Informații de contact

Acest supliment a fost dezvoltat de José Manuel Delicado. Dacă vreți să îl
contactați, trimiteți un e-mail la jm.delicado@nvda.es, sau raportați un bug
pe Github la https://github.com/jmdaweb/enhancedAria

## Noutăți

### Versiunea 2.8

* Traduceri noi și actualizate.
* S-a actualizat compatibilitatea pentru versiunile recente de NVDA.

### Versiunea 2.7

* S-a actualizat compatibilitatea pentru versiunile recente de NVDA.
* Traduceri noi și actualizate.

### Versiunea 2.6

* S-a actualizat compatibilitatea pentru versiunile recente de NVDA. Această
  versiune este compatibilă numai cu NVDA 2017.4 și versiunile mai noi.
* Traduceri noi și actualizate.
* Acum, configurația se aplică automat după comutarea profilurilor NVDA și
  restaurarea setărilor din fabrică.

### Versiunea 2.5

* S-a actualizat compatibilitatea pentru versiunile recente de NVDA.

### Versiunea 2.4

* Acum, setările sunt șterse doar la dezinstalarea
  suplimentului. Configurația nu mai este resetată la actualizare.
* Traduceri noi și actualizate.

### Versiunea 2.3

* S-a adăugat compatibilitatea cu versiunile recente de NVDA.
* Traduceri noi.

### Versiunea 2.2

* S-a reparat o eroare fatală care avea loc atunci când se utiliza un afișaj
  Braille. Mai exact, rolul articolului era configurat pentru a fi raportat.

### Versiunea 2.1

* Îmbunătățiri de stabilitate

### Versiunea 2.0

* S-a adăugat suportul pentru dialogul bazat pe setări grupate pe mai multe
  categorii disponibil în NVDA 2018.2 sau mai nou
* S-a adăugat compatibilitatea Python 3
* Acum, modulul guiHelper este folosit pentru a crea interfața suplimentului

### Versiunea 1.3

* S-a adăugat specificația configobj pentru setările suplimentului

### Versiunea 1.2

* Erori reparate

### Versiunea 1.1

* Au fost reparate erori care preveneau deschiderea dialogul de setări ale
  suplimentului când se revenea la configurația salvată a NVDA-ului

[[!tag dev stable legacy]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
