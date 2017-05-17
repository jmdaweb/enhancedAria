# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
# add-on Name
	"addon_name" : "enhancedAria",
	# Add-on description
	# TRANSLATORS: Summary for this add-on to be shown on installation and add-on informaiton.
	"addon_summary" : _("Enhanced Aria"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on installation and add-on information
	"addon_description" : _(""" This addon allows you to specify which Aria landmarks will be spoken when browsing a website.
It has support for extra aria landmarks which are not included by default in NVDA."""),
	# version
	"addon_version" : "1.1-dev",
	# Author(s)
	"addon_author" : "Jose Manuel Delicado <jmdaweb@hotmail.com>",
# URL for the add-on documentation support
	"addon_url" : None,
	"addon_docFileName" : "readme.html",
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = ["addon/globalPlugins/*", "addon/*.py"]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

excludedFiles=["doc/*/*.md"]
