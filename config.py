#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, configobj
import sqlite3

__file__ = "config.ini"

if not os.path.isfile(__file__):
	config = configobj.ConfigObj()
	config.filename = __file__

	config['Paths'] = {}
	config['Paths']['music'] = ''
	config['Paths']['playlists'] = ''
	config['Paths']['messages'] = ''
	
	config['System'] = {}
	config['System']['port'] = '80'
	config['System']['rfidreader'] = '/dev/input/event0'
	config['System']['database'] = 'cards.sqlite'
	config.write()
	
def read(configfile):
	global config

	# try to read in the config
	try:
		config = configobj.ConfigObj(configfile)
		root = [config['Paths']['music'], config['Paths']['playlists'], config['Paths']['messages']]
		
	except (IOError, KeyError, AttributeError) as e:
		print("Unable to successfully read config file: %s" % configfile)
