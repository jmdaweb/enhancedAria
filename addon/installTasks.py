#Enhanced Aria addon for NVDA
#This file is covered by the GNU General Public License.
#See the file COPYING.txt for more details.
#Copyright (C) 2017 Jose Manuel Delicado <jmdaweb@hotmail.com>

import config
def onUninstall():
	for k, v in list(config.conf._profileCache.items()):
		try:
			del config.conf._profileCache[k]['aria']
		except:
			pass
	config.conf.save()
