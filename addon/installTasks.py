import config
def onInstall():
	defaults = {
		"reportBanner":True,
		"reportMain":True,
		"reportContentinfo":True,
		"reportNavigation":True,
		"reportComplementary":True,
		"reportSearch":True,
		"reportForm":True,
		"reportArticle":False,
		"reportRegion":True
	}
	config.conf['aria']=defaults
	config.conf.save()
def onUninstall():
	for k, v in config.conf._profileCache.iteritems():
		try:
			del config.conf._profileCache[k]['aria']
		except:
			pass
	config.conf.save()
