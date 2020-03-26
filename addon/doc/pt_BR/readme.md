# Melhoramentos de Aria (Enhanced Aria) #

* Autor: José Manuel Delicado
* Complemento legado: NVDA 2019.3 e posteriores podem ler artigos na web
* Compatibilidade com NVDA: 2017.4 a 2019.2
* Baixe a [versão estável][1]

Esse complemento permite que você personalize quais marcos aria são
informados pelo NVDA quando você navega na Internet.

Sua funcionalidade é muito simples. Uma vez instalado, abra o seu navegador
e visite a web normalmente. Os marcos (pontos de referência) aria padrão
relatados pelo Firefox e pelo Chrome também estarão visíveis no Internet
Explorer, portanto poderá pressionar as teclas de navegação rápida para
alternar entre eles e listá-los pressionando NVDA+f7 em todos os
navegadores. Leia o Guia do Usuário do NVDA para mais informações.

O complemento adiciona um marco extra não incluído por padrão no NVDA, o
artigo (abreviado em Braille como art).

## O diálogo de configuração

Pode ativar ou desativar pontos de referência (marcos) acessando o NVDA,
preferências, Configurações de Aria Otimizada ou da categoria apropriada na
caixa de diálogo Opções do NVDA. O diálogo possui uma caixa de seleção para
cada marco. Se você desativar um marco, não poderá pular para ele
pressionando a tecla d ao navegar em uma página Web, e o NVDA não o
informará.

## Informação de contato

Esse complemento foi desenvolvido por José Manuel Delicado. Se quiser entrar
em contato comigo, envie um e-mail para jm.delicado@nvda.es, ou abra um
problema no GitHub em https://github.com/jmdaweb/enhancedAria

## Registro de alterações

### Versão 2.8

* Traduções novas e atualizadas.
* Atualizado sinalizadores (flags) de compatibilidade NVDA.

### Versão 2.7

* Sinalizadores de compatibilidade atualizados para versões recentes do
  NVDA.
* Traduções novas e atualizadas.

### Versão 2.6

* Sinalizadores de compatibilidade atualizados para versões recentes do
  NVDA. Essa versão é compatível apenas com o NVDA 2017.4 e superior.
* Traduções novas e atualizadas.
* Agora, a configuração é aplicada automaticamente, após alternar os perfis
  do NVDA e restaurar as configurações para os padrões originais.

### Versão 2.5

* Sinalizadores de compatibilidade atualizados para versões recentes do
  NVDA.

### Versão 2.4

* Agora, as configurações são removidas somente quando o complemento é
  desinstalado. A configuração não é mais redefinida durante a atualização.
* Traduções novas e atualizadas.

### Versão 2.3

* Acrescentada compatibilidade com as versões recentes do NVDA.
* Novas Traduções.

### Versão 2.2

* Corrigido um erro fatal que ocorria quando uma Linha Braille era usada e a
  função de artigo era configurada para ser relatada.

### Versão 2.1

* Melhorias de estabilidade

### Versão 2.0

* Adicionado suporte para o diálogo de configurações multicategoria
  disponível no NVDA 2018.2 e posteriores
* Adicionada compatibilidade com o Python 3
* Agora o módulo guiHelper é usado para criar a interface do complemento

### Versão 1.3

* Adicionado especificação de configuração de objetos para configurações do
  complemento

### Versão 1.2

* Falhas corrigidas

### Versão 1.1

* Corrigidos problemas que impediam a abertura da caixa de diálogo de
  configurações do complemento ao reverter para a configuração salva do NVDA

[[!tag dev stable legacy]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
