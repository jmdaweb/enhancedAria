# Enhanced Aria #

* Autor: José Manuel Delicado
* Compatibilidade con NVDA: da 2017.3 á 2019.1
* Descargar [versión estable][1]

Este complemento permíteche persoalizar que pontos de referencia aria
anuncia o NVDA cando navegues polo Internet.

A súa funcionalidade é moi sinxela. Unha vez instalado, abre o teu navegador
web e  visita as webs normalmente. Os pontos de referencia aria anunciados
de xeito predeterminado polo Firefox e polo Chrome tamén serán visibles no
Internet Explorer, así poderás premer as teclas de navegación rápida para
saltar entre eles, e listalos premendo NVDA+f7 en todos os navegadores. Le a
Guía do Usuario do NVDA para máis información.

O complemento engade un ponto de referencia extra que non se inclúe por
defecto no NVDA, o artigo (abreviado en braille como art).

## O diálogo Configuración

Podes habilitar ou deshabilitar pontos de referencia indo cara NVDA,
preferencias, Opcións de Enhanced Aria ou dende a categoría correspondente
no diálogo de opcións do NVDA. O diálogo ten unha caixa de verificación para
cada ponto de referencia. Se deshabilitas un ponto de referencia, non
poderás saltar cara el premendo a tecla d cando navegues por unha páxina
web, e o NVDA non o anunciará.

## Información de contacto

Este complemento foi desenvolvido por José Manuel Delicado. Se queres
contactalo, envía un correo electrónico a jm.delicado@nvda.es, ou abre un
issue en GitHub en https://github.com/jmdaweb/enhancedAria

## Rexistro de cambios

### Version 2.5

* Updated compatibility flags for recent NVDA versions.

### Versión 2.4

* Agora a configuración só se borra ao desinstalar o complemento, xa non se
  restablece ao actualizalo.
* Traducións novas e actualizadas.

### Versión 2.3

* Engadida compatibilidade con versións recentes de NVDA.
* Novas traducións.

### Versión 2.2

* Arranxado un erro fatal ao estar en uso unha pantalla braille e
  configurado o roll artigo para ser reportado.

### Versión 2.1

* Melloras de estabilidade

### Versión 2.0

* Engadido soporte para o diálogo de opcións multicategoría dispoñible en
  NVDA 2018.2 e posterior.
* Engadida compatibilidade co Python3
* Agora úsase o módulo guiHelper para crear a interface do complemento

### Versión 1.3

* Engadida especificación configobj para as preferencias do complemento

### Versión 1.2

* Correxidos fallos

### Versión 1.1

* Correxidos problemas que preveñen a apertura do diálogo de opcións do
  complemento ao voltar á configuración gardada do NVDA

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
