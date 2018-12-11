* Author: Jose Manuel Delicado
* NVDA compatibility: 2017.3 to 2019.1
* Download [stable version][1]

This addon allows you to customize which aria landmarks are reported by NVDA when you browse the Internet.

Its functionality is very simple. Once installed, open your webbrowser and visit the web as usual. The default aria landmarks reported by Firefox and Chrome will also be visible in Internet Explorer, so you will be able to press quick navigation keys to jump between them, and list them by pressing NVDA+f7 in all browsers. Read the NVDA User Guide for more information.

The addon adds an extra landmark not included by default in NVDA, the article (abbreviated in Braille as art).

## The configuration dialog

You can enable or disable landmarks by going to NVDA, preferences, Enhanced Aria Settings or from the appropriate category in the NVDA options dialog. The dialog has a checkbox for each landmark. If you disable a landmark, you won't be able to jump to it pressing the d key when browsing a webpage, and NVDA won't report it.

## Contact info

This addon has been developed by Jose Manuel Delicado. If you want to contact me, send an e-mail to jm.delicado@nvda.es, or open an issue on GitHub at https://github.com/jmdaweb/enhancedAria

## Changelog

### Version 2.3

* Added compatibility with recent NVDA releases.
* New translations.

### Version 2.2

* Fixed a fatal error when a Braille display was used and the article role was configured to be reported.

### Version 2.1

* Stability improvements

### Version 2.0

* Added support for multi-category settings dialog available on NVDA 2018.2 and later
* Added Python 3 compatibility
* Now guiHelper module is used to create the addon interface

### Version 1.3

* Added configobj specification for addon settings

### Version 1.2

* Bugs fixed

### Version 1.1

* Fixed issues which prevented opening the addon settings dialog when reverting to NVDA saved configuration

[1]: https://addons.nvda-project.org/files/get.php?file=earia
