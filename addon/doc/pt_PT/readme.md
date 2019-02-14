# àrea Realçada #

* Autor: José Manuel Delicado
* Compatibilidade com NVDA: 2017.3 a 2019.1
* Baixar [versão estável][1]

Este extra permite personalizar quais os marcadores que são reportados pelo
NVDA quando navega na Internet.

A sua funcionalidade é muito simples. Uma vez instalado o extra, abra o seu
navegador e visite a web como de costume. Os pontos de referência da ária
padrão relatados pelo Firefox e pelo Chrome também estarão visíveis no
Internet Explorer, portanto, poderá pressionar as teclas de navegação rápida
para alternar entre eles e listá-los pressionando NVDA + f7 em todos os
navegadores. Leia o Guia do Usuário do NVDA para mais informações.

O Extra adiciona um marcador extra não incluído por padrão no NVDA, o artigo
(abreviado em Braille como arte).

## O diálogo de configuração

Pode activar ou desactivar os pontos de referência, acedendo ao menu do
NVDA, preferências e as configurações avançadas do extra  Área
Realçada. Esta caixa de diálogo tem uma caixa de selecção para cada ponto de
referência. Se desabilitar um ponto de referência, não será possível saltar
para ele pressionando a tecla d ao navegar numa página da Web, e o NVDA não
o indicará.

## Informação de contacto

Este extra foi desenvolvido por José Manuel Delicado. Se quiser entrar em
contato comigo, envie um e-mail para jmdaweb@hotmail.com ou abra um problema
no GitHub em https://github.com/jmdaweb/enhancedAria

## Alterações:

### Version 2.5

* Updated compatibility flags for recent NVDA versions.

### Versão 2.4

* Agora, as configurações são removidas somente quando o extra é
  desinstalado. A configuração não é mais redefinida durante a actualização.
* Novas Traduções, adicionadas e actualizadas:

### Versão 2.3

* Acrescentada compatibilidade com as versões recentes do NVDA 
* Novas Traduções:

### Versão 2.2

* Corrigido um erro fatal que ocorria quando uma exibição em Braille era
  usada e a função de artigo era configurada para ser relatada.

### Versão 2.1

* Melhorias de estabilidade

### Versão 2.0

* Adicionado suporte para o diálogo de configurações multi-categoria
  disponível no NVDA 2018.2 e posterior
* Adicionada compatibilidade com o Python 3
* Agora o módulo guiHelper é usado para criar a interface do extra

### Versão 1.3

* Adicionado especificação de configuração de objectos para configurações do
  extra

### Versão 1.2

* Solução de bugs.

### Versão 1.1

* Corrigidos problemas que impediam a abertura da caixa de diálogo de
  configurações do extra ao reverter para a configuração guardada do NVDA

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
