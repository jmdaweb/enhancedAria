# Enhanced Aria #

* Autor: Jose Manuel Delicado
* Przestarzały dodatek: NVDA 2019.3 może odczytywać artykuły na stronach
* Zgodność z wersjami NVDA: 2017.4 do 2019.2
* Pobierz [wersja stabilna][1]

Ten dodatek pozwala określić, które punkty orientacyjne mają być wymawiane
przez NVDA podczas przeglądania Internetu.

Działa on w bardzo prosty sposób. Po zainstalowaniu dodatku, otwórz
przeglądarkę internetową i odwiedzaj strony tak jak zawsze. Domyślne punkty
orientacyjne wymawiane w przeglądarkach Firefox i Chrome będą widoczne
również w Internet Explorer. Można więc naciskać klawisze szybkiej
nawigacji, aby przeskakiwać między punktami orientacyjnymi i dodawać je do
listy naciskając NVDA+f7 we wszystkich przeglądarkach. Więcej informacji
można znaleźć w Podręczniku Użytkownika NVDA.

Enhanced Aria wprowadza do NVDA dodatkowy punkt orientacyjny, którego
domyślnie tam nie ma. Jest to artykuł, wyświetlany w brajlu jako skrót art.

## Dialog ustawień

Punkty orientacyjne można wyłączyć z poziomu menu NVDA, ustawienia,
ustawienia Enhanced Aria lub w odpowiedniej kategorii dialogu ustawień
NVDA. Każdy punkt orientacyjny posiada pole wyboru. Jeśli punkt orientacyjny
zostanie wyłączony, nie będzie już można do niego dotrzeć literą d podczas
przeglądania strony internetowej. NVDA nie będzie go też wymawiać.

## Dane kontaktowe

Ten dodatek rozwija Jose Manuel Delicado. Jeśli chcesz się ze mną
skontaktować, wyślij e-mail na adres jm.delicado@nvda.es, lub utwórz temat w
GitHubie na stronie https://github.com/jmdaweb/enhancedAria

## Lista zmian

### Wersja 2.8

* Nowe i zaktualizowane tłumaczenia.
* Zaktualizowano flagi zgodności.

### Wersja 2.7

* Dodano zgodność z najnowszymi wersjami NVDA.
* Nowe i zaktualizowane tłumaczenia.

### Wersja 2.6

* Zaktualizowano flagi zgodności z ostatnimi wersjami NVDA. Ta wersja jest
  zgodna tylko z wersjami NVDA 2017.4 i nowszymi.
* Nowe i zaktualizowane tłumaczenia.
* Od teraz konfiguracja jest automatycznie zastosowana po przełączeniu
  plofilów NVDA i przywróceniu ustawień do wartości domyślnych.

### Versja 2.5

* Dodano zgodność z najnowszymi wersjami NVDA.

### Versja 2.4

* Od teraz ustawienia usuwają się tylko po odinstalowaniu dodatku. Ponadto,
  nie resetują się już po aktualizacji.
* Nowe i zaktualizowane tłumaczenia.

### Wersja 2.3

* Dodana zgodność z nowszymi wersjami NVDA.
* Nowe tłumaczenia.

### Wersja 2.2

* Naprawiono poważny błąd, który pojawiał się gdy używany był monitor
  brajlowski i ustawione było wymawianie artykułu.

### Wersja 2.1

* Ulepszenia stabilności

### Wersja 2.0

* Dodano wsparcie dla panelu ustawień dostępnego w NVDA 2018.2 i nowszych.
* Dodano zgodność z Pythonem 3
* Od teraz do tworzenia interfejsu dodatku używany będzie guiHelper module

### Wersja 1.3

* Dodano specyfikację configobj dla ustawień dodatku

### Wersja 1.2

* Poprawiono błędy

### Wersja 1.1

* Naprawiono błędy, które uniemożliwiały otwarcie dialogu ustawień dodatku
  przy powrocie do zapisanych ustawień NVDA

[[!tag dev stable legacy]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
