#Enhanced Aria addon for NVDA
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2017 Jose Manuel Delicado <jmdaweb@hotmail.com>

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
