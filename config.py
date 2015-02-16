#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, configobj

__file__ = "config.ini"

if not os.path.isfile(__file__):
	config = configobj.ConfigObj()
	config.filename = __file__

	config['Section'] = {}
	config['Section']['item'] = 'something'
	config.write()

def read(configfile):
	global config

	# try to read in the config
	try:
		config = configobj.ConfigObj(configfile)
		
	except (IOError, KeyError, AttributeError) as e:
		print("Unable to successfully read config file: %s" % configfile)
