# Aria mejorada

Versión 2.2

## Introducción

Este complemento te permite configurar qué puntos de referencia Aria se anuncian cuando navegas por Internet.

Su funcionamiento es muy simple. Una vez instalado, abre tu navegador web y visita la web como siempre. Los puntos de referencia Aria anunciados por defecto  en Firefox y Chrome también serán visibles en Internet Explorer, por lo que podrás pulsar teclas rápidas de navegación para saltar entre ellos, y listarlos pulsando NVDA+f7 en todos los navegadores. Lee la guía de usuario de NVDA para más información.

El complemento añade un punto de referencia extra que no viene incluido por defecto en NVDA, el artículo (abreviado en Braille como art).

## El diálogo de configuración

Puedes activar o desactivar puntos de referencia yendo a NVDA, preferencias, Ajustes de Aria mejorada o desde la categoría correspondiente en el diálogo de opciones de NVDA. El diálogo tiene una casilla de verificación por cada punto de referencia. Si desactivas un punto de referencia, no podrás saltar a él pulsando la letra d al explorar una página web, y NVDA no lo anunciará.

## Información de contacto

Este complemento ha sido desarrollado por José Manuel Delicado. Si quieres contactar conmigo, envía un e-mail a jm.delicado@nvda.es, o abre una incidencia en GitHub en https://github.com/jmdaweb/enhancedAria

## Registro de cambios

### Versión 2.2

* Se ha solucionado un error fatal que se producía al usar una pantalla Braille si la verbalización de artículos estaba activada.

### Versión 2.1

* Mejoras de estabilidad

### Versión 2.0

* Se ha añadido soporte para el nuevo diálogo multicategoría disponible en NVDA 2018.2 y versiones posteriores
* Se ha añadido compatibilidad con Python 3
* Ahora se usa el módulo guiHelper para crear la interfaz del complemento

### Versión 1.3

* Se ha agregado una especificación de configobj para los ajustes del complemento

### Versión 1.2

* Errores corregidos

### Versión 1.1

* Corregidos errores que impedían abrir el diálogo de configuración al regresar a la configuración guardada de NVDA

