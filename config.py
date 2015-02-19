#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, configobj
import sqlite3

script_path = os.path.dirname(os.path.abspath(__file__))
cfgfile = "%s/config.ini" % script_path

if not os.path.isfile(cfgfile):
	config = configobj.ConfigObj()
	config.filename = cfgfile

	config['Paths'] = {}
	config['Paths']['music'] = '/media/Music/music'
	config['Paths']['playlists'] = '/home/pi/playlists'
	config['Paths']['messages'] = '/home/pi/mplayer-web-rfid-control/messages'
	
	config['System'] = {}
	config['System']['port'] = '8080'
	config['System']['rfidreader'] = '/dev/input/event0'
	config['System']['database'] = "%s/cards.sqlite" % script_path
	config['System']['root'] = [config['Paths']['music'], config['Paths']['playlists'], config['Paths']['messages']]
	config.write()
	
def read(cfgfile):
	global config

	# try to read in the config
	try:
		config = configobj.ConfigObj(cfgfile)
		
	except (IOError, KeyError, AttributeError) as e:
		print("Unable to successfully read config file: %s" % cfgfile)
