# Enhanced Aria #

* Autor: José Manuel Delicado
* Compatibilidad con NVDA: de 2017.4 a 2019.2
* Descargar [versión estable][1]

Este complemento te permite personalizar qué puntos de referencia aria
anuncia NVDA cuando navegues por Internet.

Su funcionalidad es muy sencilla. Una vez instalado, abre tu navegador web y
visita las webs normalmente. Los puntos de referencia aria anunciados de
manera predeterminada por Firefox y Chrome también serán visibles en
Internet Explorer, así podrás pulsar las teclas de navegación rápida para
saltar entre ellos, y listarlos pulsando NVDA+f7 en todos los
navegadores. Lee la Guía del Usuario de NVDA para más información.

El complemento añade un punto de referencia extra que no se incluye por
defecto en NVDA, El artículo (abreviado en Braille como art).

## El diálogo Configuración

Puedes habilitar o deshabilitar puntos de referencia yendo a NVDA,
preferencias, Ajustes de Aria mejorada o desde la categoría correspondiente
del diálogo de opciones de NVDA. El diálogo tiene una casilla de
verificación para cada punto de referencia. Si deshabilitas un punto de
referencia, no podrás saltar a él pulsando la tecla d cuando navegues por
una página web, y NVDA no lo anunciará.

## Información de contacto

Este complemento ha sido desarrollado por José Manuel Delicado. Si quieres
contactarlo, envía un correo electrónico a jm.delicado@nvda.es, o abre una
incidencia en GitHub en https://github.com/jmdaweb/enhancedAria

## Registro de cambios

### Versión 2.7

* Se han actualizado los indicadores de compatibilidad con versiones
  recientes de NVDA.
* Nuevas traducciones y traducciones actualizadas.

### Versión 2.6

* Se han actualizado los indicadores de compatibilidad con versiones
  recientes de NVDA. Esta versión tan sólo es compatible con NVDA 2017.4 y
  versiones posteriores.
* Nuevas traducciones y traducciones actualizadas.
* Ahora se aplica la configuración automáticamente después de cambiar de
  perfil o restablecer los ajustes a valores de fábrica.

### Versión 2.5

* Se han actualizado los indicadores de compatibilidad con versiones
  recientes de NVDA.

### Versión 2.4

* Ahora, los ajustes se eliminan sólo al desinstalar el complemento. La
  configuración ya no se restablece al actualizar.
* Nuevas traducciones y traducciones actualizadas.

### Versión 2.3

* Añadida compatibilidad con versiones recientes de NVDA.
* Nuevas traducciones.

### Versión 2.2

* Se ha solucionado un error fatal que se producía al usar una pantalla
  Braille si la verbalización de artículos estaba activada.

### Versión 2.1

* Mejoras de estabilidad

### Versión 2.0

* Se ha añadido soporte para el nuevo diálogo multicategoría disponible en
  NVDA 2018.2 y versiones posteriores
* Se ha añadido compatibilidad con Python 3
* Ahora se usa el módulo guiHelper para crear la interfaz del complemento

### Versión 1.3

* Se ha añadido una especificación de ConfigObj para los ajustes del
  complemento

### Versión 1.2

* Corregidos fallos

### Versión 1.1

* Corregidos problemas que previenen la apertura del diálogo de opciones del
  complemento al volver a la configuración guardada de NVDA

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
