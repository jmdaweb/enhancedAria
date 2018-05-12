#Enhanced Aria addon for NVDA
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2018 Jose Manuel Delicado <jm.delicado@nvda.es>

import aria
orig_roles=aria.landmarkRoles.copy()
orig_html=aria.htmlNodeNameToAriaLandmarkRoles.copy()
import addonHandler
addonHandler.initTranslation()
import globalPluginHandler
import config
import gui
from gui import settingsDialogs
try:
	from gui import NVDASettingsDialog
except:
	pass
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
	if config.conf['aria']['reportBanner']==True:
		conf_aria['banner']=orig_roles['banner']
		conf_html['header']='banner'
	if config.conf['aria']['reportMain']==True:
		conf_aria['main']=orig_roles['main']
		conf_html['main']='main'
	if config.conf['aria']['reportNavigation']==True:
		conf_aria['navigation']=orig_roles['navigation']
		conf_html['nav']='navigation'
	if config.conf['aria']['reportContentinfo']==True:
		conf_aria['contentinfo']=orig_roles['contentinfo']
		conf_html['footer']='contentinfo'
	if config.conf['aria']['reportSearch']==True:
		conf_aria['search']=orig_roles['search']
	if config.conf['aria']['reportForm']==True:
		conf_aria['form']=orig_roles['form']
		conf_html['form']='form'
	if config.conf['aria']['reportComplementary']==True:
		conf_aria['complementary']=orig_roles['complementary']
		conf_html['aside']='complementary'
	if config.conf['aria']['reportRegion']==True:
		conf_aria['region']=orig_roles['region']
		conf_html['section']='region'
	if config.conf['aria']['reportArticle']==True:
		#TRANSLATORS: An article element inside a document
		conf_aria['article']=_(u"article")
		conf_html['article']='article'
	aria.landmarkRoles=conf_aria
	aria.htmlNodeNameToAriaLandmarkRoles=conf_html

# Common functions for dialog and panel classes to create and retrieve settings
def createSettings(obj, sizer):
	#TRANSLATORS: report banners checkbox
	obj.bannerenabled=wx.CheckBox(obj, wx.NewId(), label=_(u"Report banners"))
	obj.bannerenabled.SetValue(config.conf['aria']['reportBanner'])
	sizer.Add(obj.bannerenabled,border=10,flag=wx.BOTTOM)
	#TRANSLATORS: report main content checkbox
	obj.mainenabled=wx.CheckBox(obj, wx.NewId(), label=_(u"Report main content"))
	obj.mainenabled.SetValue(config.conf['aria']['reportMain'])
	sizer.Add(obj.mainenabled,border=10,flag=wx.BOTTOM)
	#TRANSLATORS: report search forms checkbox
	obj.searchenabled=wx.CheckBox(obj, wx.NewId(), label=_(u"Report search forms"))
	obj.searchenabled.SetValue(config.conf['aria']['reportSearch'])
	sizer.Add(obj.searchenabled,border=10,flag=wx.BOTTOM)
	#TRANSLATORS: report forms with form role checkbox
	obj.formenabled=wx.CheckBox(obj, wx.NewId(), label=_(u"Report forms with form role"))
	obj.formenabled.SetValue(config.conf['aria']['reportForm'])
	sizer.Add(obj.formenabled,border=10,flag=wx.BOTTOM)
	#TRANSLATORS: report navigation areas checkbox
	obj.navigationenabled=wx.CheckBox(obj, wx.NewId(), label=_(u"Report navigation areas"))
	obj.navigationenabled.SetValue(config.conf['aria']['reportNavigation'])
	sizer.Add(obj.navigationenabled,border=10,flag=wx.BOTTOM)
	#TRANSLATORS: report complementary content checkbox
	obj.complementaryenabled=wx.CheckBox(obj, wx.NewId(), label=_(u"Report complementary content"))
	obj.complementaryenabled.SetValue(config.conf['aria']['reportComplementary'])
	sizer.Add(obj.complementaryenabled,border=10,flag=wx.BOTTOM)
	#TRANSLATORS: report content info checkbox
	obj.contentinfoenabled=wx.CheckBox(obj, wx.NewId(), label=_(u"Report content info areas"))
	obj.contentinfoenabled.SetValue(config.conf['aria']['reportContentinfo'])
	sizer.Add(obj.contentinfoenabled,border=10,flag=wx.BOTTOM)
	#TRANSLATORS: report articles checkbox
	obj.articleenabled=wx.CheckBox(obj, wx.NewId(), label=_(u"Report articles"))
	obj.articleenabled.SetValue(config.conf['aria']['reportArticle'])
	sizer.Add(obj.articleenabled,border=10,flag=wx.BOTTOM)
	#TRANSLATORS: report other labelled regions checkbox
	obj.regionenabled=wx.CheckBox(obj, wx.NewId(), label=_(u"Report other labelled regions"))
	obj.regionenabled.SetValue(config.conf['aria']['reportRegion'])
	sizer.Add(obj.regionenabled,border=10,flag=wx.BOTTOM)

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
			self.prefsMenu = gui.mainFrame.sysTrayIcon.menu.GetMenuItems()[0].GetSubMenu()
			#TRANSLATORS: The configuration option in NVDA Preferences menu
			self.enhancedAriaSettingsItem = self.prefsMenu.Append(wx.ID_ANY, _(u"Enhanced aria settings..."), _(u"Change enhanced Aria settings"))
			gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onEnhancedAriaMenu, self.enhancedAriaSettingsItem)

	def terminate(self):
		try:
			aria.landmarkRoles=orig_roles
			aria.htmlNodeNameToAriaLandmarkRoles=orig_html
			if hasattr(settingsDialogs, 'SettingsPanel'):
				NVDASettingsDialog.categoryClasses.remove(enhancedAriaPanel)
			else:
				self.prefsMenu.RemoveItem(self.enhancedAriaSettingsItem)
		except:
			pass

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

class enhancedAriaPanel(settingsDialogs.SettingsPanel):
	title=addonSettingsTitle

	def makeSettings(self, sizer):
		createSettings(self, sizer)

	def onSave(self):
		storeSettings(self)
