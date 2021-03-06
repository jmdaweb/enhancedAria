#Enhanced Aria addon for NVDA
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2019 Jose Manuel Delicado <jm.delicado@nvda.es>

import aria
import braille
orig_roles=aria.landmarkRoles.copy()
orig_html=aria.htmlNodeNameToAriaLandmarkRoles.copy()
orig_braille=braille.landmarkLabels.copy()
import addonHandler
addonHandler.initTranslation()
import globalPluginHandler
import config
import gui
from gui import settingsDialogs, guiHelper
try:
	from gui import NVDASettingsDialog
	from gui.settingsDialogs import SettingsPanel
except:
	SettingsPanel=object # give the panel class something it can inherit from
import wx

#TRANSLATORS: Settings dialog and/or panel title
addonSettingsTitle=_("Enhanced Aria settings")

confspec={
	"reportBanner":"boolean(default=true)",
	"reportMain":"boolean(default=true)",
	"reportContentinfo":"boolean(default=true)",
	"reportNavigation":"boolean(default=true)",
	"reportComplementary":"boolean(default=true)",
	"reportSearch":"boolean(default=true)",
	"reportForm":"boolean(default=true)",
	"reportArticle":"boolean(default=false)",
	"reportRegion":"boolean(default=true)"
}
config.conf.spec['aria']=confspec

def applyConfig():
	conf_aria={}
	conf_html={}
	conf_braille={}
	if config.conf['aria']['reportBanner']:
		conf_aria['banner']=orig_roles['banner']
		conf_html['header']='banner'
		conf_braille['banner']=orig_braille['banner']
	if config.conf['aria']['reportMain']:
		conf_aria['main']=orig_roles['main']
		conf_html['main']='main'
		conf_braille['main']=orig_braille['main']
	if config.conf['aria']['reportNavigation']:
		conf_aria['navigation']=orig_roles['navigation']
		conf_html['nav']='navigation'
		conf_braille['navigation']=orig_braille['navigation']
	if config.conf['aria']['reportContentinfo']:
		conf_aria['contentinfo']=orig_roles['contentinfo']
		conf_html['footer']='contentinfo'
		conf_braille['contentinfo']=orig_braille['contentinfo']
	if config.conf['aria']['reportSearch']:
		conf_aria['search']=orig_roles['search']
		conf_braille['search']=orig_braille['search']
	if config.conf['aria']['reportForm']:
		conf_aria['form']=orig_roles['form']
		conf_html['form']='form'
		conf_braille['form']=orig_braille['form']
	if config.conf['aria']['reportComplementary']:
		conf_aria['complementary']=orig_roles['complementary']
		conf_html['aside']='complementary'
		conf_braille['complementary']=orig_braille['complementary']
	if config.conf['aria']['reportRegion']:
		conf_aria['region']=orig_roles['region']
		conf_html['section']='region'
		conf_braille['region']=orig_braille['region']
	if config.conf['aria']['reportArticle']:
		#TRANSLATORS: An article element inside a document
		conf_aria['article']=_("article")
		conf_html['article']='article'
		#TRANSLATORS: Braille abbreviation for an article element inside a document
		conf_braille['article']=_("art")
	aria.landmarkRoles=conf_aria
	aria.htmlNodeNameToAriaLandmarkRoles=conf_html
	braille.landmarkLabels=conf_braille

# Common functions for dialog and panel classes to create and retrieve settings
def createSettings(obj, sizer):
	helper=guiHelper.BoxSizerHelper(obj, sizer=sizer)
	#TRANSLATORS: report banners checkbox
	obj.bannerenabled=helper.addItem(wx.CheckBox(obj, wx.ID_ANY, label=_("Report banners")))
	obj.bannerenabled.SetValue(config.conf['aria']['reportBanner'])
	#TRANSLATORS: report main content checkbox
	obj.mainenabled=helper.addItem(wx.CheckBox(obj, wx.ID_ANY, label=_("Report main content")))
	obj.mainenabled.SetValue(config.conf['aria']['reportMain'])
	#TRANSLATORS: report search forms checkbox
	obj.searchenabled=helper.addItem(wx.CheckBox(obj, wx.ID_ANY, label=_("Report search forms")))
	obj.searchenabled.SetValue(config.conf['aria']['reportSearch'])
	#TRANSLATORS: report forms with form role checkbox
	obj.formenabled=helper.addItem(wx.CheckBox(obj, wx.ID_ANY, label=_("Report forms with form role")))
	obj.formenabled.SetValue(config.conf['aria']['reportForm'])
	#TRANSLATORS: report navigation areas checkbox
	obj.navigationenabled=helper.addItem(wx.CheckBox(obj, wx.ID_ANY, label=_("Report navigation areas")))
	obj.navigationenabled.SetValue(config.conf['aria']['reportNavigation'])
	#TRANSLATORS: report complementary content checkbox
	obj.complementaryenabled=helper.addItem(wx.CheckBox(obj, wx.ID_ANY, label=_("Report complementary content")))
	obj.complementaryenabled.SetValue(config.conf['aria']['reportComplementary'])
	#TRANSLATORS: report content info checkbox
	obj.contentinfoenabled=helper.addItem(wx.CheckBox(obj, wx.ID_ANY, label=_("Report content info areas")))
	obj.contentinfoenabled.SetValue(config.conf['aria']['reportContentinfo'])
	#TRANSLATORS: report articles checkbox
	obj.articleenabled=helper.addItem(wx.CheckBox(obj, wx.ID_ANY, label=_("Report articles")))
	obj.articleenabled.SetValue(config.conf['aria']['reportArticle'])
	#TRANSLATORS: report other labelled regions checkbox
	obj.regionenabled=helper.addItem(wx.CheckBox(obj, wx.ID_ANY, label=_("Report other labelled regions")))
	obj.regionenabled.SetValue(config.conf['aria']['reportRegion'])

def storeSettings(obj):
	config.conf['aria']['reportBanner']=obj.bannerenabled.GetValue()
	config.conf['aria']['reportMain']=obj.mainenabled.GetValue()
	config.conf['aria']['reportSearch']=obj.searchenabled.GetValue()
	config.conf['aria']['reportForm']=obj.formenabled.GetValue()
	config.conf['aria']['reportNavigation']=obj.navigationenabled.GetValue()
	config.conf['aria']['reportComplementary']=obj.complementaryenabled.GetValue()
	config.conf['aria']['reportContentinfo']=obj.contentinfoenabled.GetValue()
	config.conf['aria']['reportArticle']=obj.articleenabled.GetValue()
	config.conf['aria']['reportRegion']=obj.regionenabled.GetValue()
	applyConfig()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		#apply saved configuration
		applyConfig()
		if hasattr(settingsDialogs, 'SettingsPanel'):
			NVDASettingsDialog.categoryClasses.append(enhancedAriaPanel)
		else:
			self.prefsMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
			#TRANSLATORS: The configuration option in NVDA Preferences menu
			self.enhancedAriaSettingsItem = self.prefsMenu.Append(wx.ID_ANY, _("Enhanced aria settings..."), _("Change enhanced Aria settings"))
			gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onEnhancedAriaMenu, self.enhancedAriaSettingsItem)
		config.post_configReset.register(applyConfig)
		if hasattr(config, 'post_configProfileSwitch'):
			config.post_configProfileSwitch.register(applyConfig)
		else:
			config.configProfileSwitched.register(applyConfig)

	def terminate(self):
		try:
			aria.landmarkRoles=orig_roles
			aria.htmlNodeNameToAriaLandmarkRoles=orig_html
			braille.landmarkLabels=orig_braille
			if hasattr(settingsDialogs, 'SettingsPanel'):
				NVDASettingsDialog.categoryClasses.remove(enhancedAriaPanel)
			else:
				self.prefsMenu.RemoveItem(self.enhancedAriaSettingsItem)
		except:
			pass
		config.post_configReset.unregister(applyConfig)
		if hasattr(config, 'post_configProfileSwitch'):
			config.post_configProfileSwitch.unregister(applyConfig)
		else:
			config.configProfileSwitched.unregister(applyConfig)

	def onEnhancedAriaMenu(self, evt):
		gui.mainFrame._popupSettingsDialog(enhancedAriaSettings)

class enhancedAriaSettings(settingsDialogs.SettingsDialog):
	title=addonSettingsTitle

	def makeSettings(self, sizer):
		createSettings(self, sizer)

	def postInit(self):
		self.bannerenabled.SetFocus()

	def onOk(self, evt):
		storeSettings(self)
		super(enhancedAriaSettings, self).onOk(evt)

class enhancedAriaPanel(SettingsPanel):
	title=addonSettingsTitle

	def makeSettings(self, sizer):
		createSettings(self, sizer)

	def onSave(self):
		storeSettings(self)
