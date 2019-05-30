# 增强aria“ #

* 作者: Jose Manuel Delicado
* NVDA compatibility: 2017.4 to 2019.2
* 下载 [稳定版][1]

此插件允许您在浏览Internet时自定义NVDA报告哪些Aria地标。

它的功能非常简单。安装后，打开浏览器并照常浏览网页。 Firefox和Chrome报告的默认aria地标也会在Internet
Explorer中显示，因此您可以按快速导航键在它们之间跳转，并在所有浏览器中按NVDA + f7列出它们。请阅读NVDA用户指南了解更多信息。

插件增加了NVDA中默认不包含的额外路标，文章（缩写为盲文作为艺术）。

## 配置

您可以通过转到NVDA，首选项，增强型Aria设置或NVDA选项对话框中的相应类别来启用或禁用地标。该对话框有一个每个地标的复选框。如果禁用地标，则在浏览网页时无法按d键跳转到该地标，NVDA将不会朗读。

## 联系信息

这个插件由Jose Manuel
Delicado开发。如果您想与我联系，请发送电子邮件至jm.delicado@nvda.es，或通过https://github.com/jmdaweb/enhancedAria在GitHub上提交问题

## 更新日志

### Version 2.6

* Updated compatibility flags for recent NVDA versions. This version is only
  compatible with NVDA 2017.4 and above.
* 新的更新和翻译。
* Now, the configuration is automatically applied after switching NVDA
  profiles and restoring settings to factory defaults.

### 版本2.5

* 更新了最新NVDA版本的兼容性标志。

### 版本2.4

* 现在，仅在卸载插件时才会删除设置。升级时，配置不再重置。
* 新的更新和翻译。

### 版本2.3

* 新增与最近NVDA版本的兼容性。
* 新的翻译。

### 版本2.2

* 修复了使用盲文显示器并将文章角色配置为报告时的致命错误。

### 版本2.1

* 稳定性改进

### 版本2.0

* 增加了对NVDA 2018.2及更高版本上可用的多分类设置对话框的支持
* 增加了Python 3的兼容性
* 现在，guiHelper模块用于创建插件界面

### 版本1.3

* 增加了用于插件设置的configobj规范

### 版本1.2

* 错误修复

### 版本1.1

* 修复了在恢复到NVDA保存配置时阻止打开插件设置对话框的问题

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=earia
