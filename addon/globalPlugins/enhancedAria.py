import aria
orig_roles=aria.landmarkRoles.copy()
orig_html=aria.htmlNodeNameToAriaLandmarkRoles.copy()
import addonHandler
addonHandler.initTranslation()
import globalPluginHandler
import config
import gui
from gui import settingsDialogs
import wx

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
		conf_aria['article']=_(u"article")
		conf_html['article']='article'
	aria.landmarkRoles=conf_aria
	aria.htmlNodeNameToAriaLandmarkRoles=conf_html

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()
		if config.conf['aria']['reportMain'] not in [True, False]:
			#convert configuration values into booleans
			self.initConfig()
		#apply saved configuration
		applyConfig()
		self.prefsMenu = gui.mainFrame.sysTrayIcon.menu.GetMenuItems()[0].GetSubMenu()
		self.enhancedAriaSettingsItem = self.prefsMenu.Append(wx.ID_ANY, _(u"Enhanced aria settings..."), _(u"Change enhanced Aria settings"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onEnhancedAriaMenu, self.enhancedAriaSettingsItem)

	def initConfig(self):
		config.conf['aria']['reportBanner']=config.conf['aria']['reportBanner']==u'True'
		config.conf['aria']['reportMain']=config.conf['aria']['reportMain']==u'True'
		config.conf['aria']['reportNavigation']=config.conf['aria']['reportNavigation']==u'True'
		config.conf['aria']['reportSearch']=config.conf['aria']['reportSearch']==u'True'
		config.conf['aria']['reportForm']=config.conf['aria']['reportForm']==u'True'
		config.conf['aria']['reportComplementary']=config.conf['aria']['reportComplementary']==u'True'
		config.conf['aria']['reportRegion']=config.conf['aria']['reportRegion']==u'True'
		config.conf['aria']['reportArticle']=config.conf['aria']['reportArticle']==u'True'
		config.conf['aria']['reportContentinfo']=config.conf['aria']['reportContentinfo']==u'True'

	def terminate(self):
		try:
			aria.landmarkRoles=orig_roles
			aria.htmlNodeNameToAriaLandmarkRoles=orig_html
			self.prefsMenu.RemoveItem(self.enhancedAriaSettingsItem)
		except:
			pass

	def onEnhancedAriaMenu(self, evt):
		gui.mainFrame._popupSettingsDialog(enhancedAriaSettings)

class enhancedAriaSettings(settingsDialogs.SettingsDialog):
	title=_(u"Enhanced Aria settings")
	def makeSettings(self, sizer):
		self.bannerenabled=wx.CheckBox(self, wx.NewId(), label=_(u"Report banners"))
		self.bannerenabled.SetValue(config.conf['aria']['reportBanner'])
		sizer.Add(self.bannerenabled,border=10,flag=wx.BOTTOM)
		self.mainenabled=wx.CheckBox(self, wx.NewId(), label=_(u"Report main content"))
		self.mainenabled.SetValue(config.conf['aria']['reportMain'])
		sizer.Add(self.mainenabled,border=10,flag=wx.BOTTOM)
		self.searchenabled=wx.CheckBox(self, wx.NewId(), label=_(u"Report search forms"))
		self.searchenabled.SetValue(config.conf['aria']['reportSearch'])
		sizer.Add(self.searchenabled,border=10,flag=wx.BOTTOM)
		self.formenabled=wx.CheckBox(self, wx.NewId(), label=_(u"Report forms with form role"))
		self.formenabled.SetValue(config.conf['aria']['reportForm'])
		sizer.Add(self.formenabled,border=10,flag=wx.BOTTOM)
		self.navigationenabled=wx.CheckBox(self, wx.NewId(), label=_(u"Report navigation areas"))
		self.navigationenabled.SetValue(config.conf['aria']['reportNavigation'])
		sizer.Add(self.navigationenabled,border=10,flag=wx.BOTTOM)
		self.complementaryenabled=wx.CheckBox(self, wx.NewId(), label=_(u"Report complementary content"))
		self.complementaryenabled.SetValue(config.conf['aria']['reportComplementary'])
		sizer.Add(self.complementaryenabled,border=10,flag=wx.BOTTOM)
		self.contentinfoenabled=wx.CheckBox(self, wx.NewId(), label=_(u"Report content info areas"))
		self.contentinfoenabled.SetValue(config.conf['aria']['reportContentinfo'])
		sizer.Add(self.contentinfoenabled,border=10,flag=wx.BOTTOM)
		self.articleenabled=wx.CheckBox(self, wx.NewId(), label=_(u"Report articles"))
		self.articleenabled.SetValue(config.conf['aria']['reportArticle'])
		sizer.Add(self.articleenabled,border=10,flag=wx.BOTTOM)
		self.regionenabled=wx.CheckBox(self, wx.NewId(), label=_(u"Report other labelled regions"))
		self.regionenabled.SetValue(config.conf['aria']['reportRegion'])
		sizer.Add(self.regionenabled,border=10,flag=wx.BOTTOM)

	def postInit(self):
		self.bannerenabled.SetFocus()

	def onOk(self, evt):
		config.conf['aria']['reportBanner']=self.bannerenabled.GetValue()
		config.conf['aria']['reportMain']=self.mainenabled.GetValue()
		config.conf['aria']['reportSearch']=self.searchenabled.GetValue()
		config.conf['aria']['reportForm']=self.formenabled.GetValue()
		config.conf['aria']['reportNavigation']=self.navigationenabled.GetValue()
		config.conf['aria']['reportComplementary']=self.complementaryenabled.GetValue()
		config.conf['aria']['reportContentinfo']=self.contentinfoenabled.GetValue()
		config.conf['aria']['reportArticle']=self.articleenabled.GetValue()
		config.conf['aria']['reportRegion']=self.regionenabled.GetValue()
		applyConfig()
		super(enhancedAriaSettings, self).onOk(evt)
