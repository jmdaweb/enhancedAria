# Enhanced Aria #

* Autor: Jose Manuel Delicado
* [Stabile Version herunterladen][1]

Mit dieser Erweiterung können Sie einstellen, welche Aria-Sprungmarken beim
Surfen im Internet von NVDA gemeldet werden.

Die Funktionsweise ist sehr einfach. Öffnen Sie nach der Installation Ihren
Webbrowser und besuchen Sie das Web wie gewohnt. Die standardmäßig von
Firefox und Chrome gemeldeten Aria-Sprungmarken werden auch im Internet
Explorer sichtbar sein, so dass Sie die Schnellnavigationstasten drücken
können, um zwischen ihnen zu springen und sie durch Drücken von NVDA+f7 in
allen Browsern aufzulisten. Lesen Sie das NVDA-Benutzerhandbuch für weitere
Informationen.

Die Erweiterung fügt eine zusätzliche Sprungmarke hinzu, die nicht
standardmäßig in NVDA enthalten ist, den Artikel (abgekürzt in Braille).

## Das Einstellungsfenster

Sie können Sprungmarken aktivieren oder deaktivieren, indem Sie zu NVDA,
Einstellungen, "Enhanced Aria"-Einstellungen oder aus der entsprechenden
Kategorie im NVDA-Optionen-Dialog gehen. Der Dialog hat für jede Sprungmarke
eine Checkbox. Wenn Sie eine Sprungmarke deaktivieren, können Sie beim
Durchsuchen einer Webseite nicht zu ihr springen und NVDA meldet sie auch
nicht.

## Kontakt-Informationen

Diese Erweiterung wurde von José Manuel Delicado entwickelt. Wenn Sie mit
mir Kontakt aufnehmen möchten, senden Sie eine E-Mail an
jm.delicado@nvda.es, oder öffnen Sie einen Fehlerbericht auf GitHub unter
https://github.com/jmdaweb/enhancedAria

## Änderungsprotokoll

### Version 2.2

* Ein kritischer Fehler wurde behoben, wenn eine Braillezeile verwendet
  wurde und die Artikelrolle so konfiguriert war, dass sie gemeldet wurde.

### Version 2.1

* Stabilitätsverbesserungen

### Version 2.0

* Unterstützung für den Multi-Kategorie-Einstellungsdialog ab NVDA 2018.2
  wurde hinzugefügt.
* Kompatibilität für Python 3 hinzugefügt
* Es wird nun das guiHelper Modul verwendet, um das Addon Interface zu
  erstellen.

### Version 1.3

* Es wurde die configobj-Spezifikation  für die Einstellungen der
  Erweiterung hinzugefügt

### Version 1.2

* Fehler wurden behoben.

### Version 1.1

* Es wurden Probleme behoben, die das Öffnen des Dialogs der
  Erweiterungseinstellungen nach dem Zurücksetzen auf die NVDA-gespeicherte
  Konfiguration verhinderten.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
