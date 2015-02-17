#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program; if not, write to the Free Software Foundation, Inc.,
#   51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
SYNOPSIS

	python addcard.py /full/path/to/directory_or_playlist [-s,--shuffle]

DESCRIPTION

	Assigns either a directory of mp3 files or a m3u playlist file to
	an RFID swipe card.

AUTHOR

	Robert Crouch (rob.crouch@gmail.com)

VERSION

	$Id$
"""

__program__ = "mplayer-web-rfid-control"
__author__ = "Robert Crouch (rob.crouch@gmail.com)"
__copyright__ = "Copyright (C) 2015- Robert Crouch"
__license__ = "LGPL 3.0"
__version__ = "v1.150216"

import os, sys, argparse, logging, logging.handlers
import config as cfg    # config related things are in config.py
						# this import will create a blank config file if it doesn't exist already

import sqlite3
from evdev import InputDevice, categorize, ecodes						

def parse_args(argv):
	""" Read in any command line options and return them
	"""

	# Define and parse command line arguments
	parser = argparse.ArgumentParser(description='Assign a playlist or folder to a card.')
	parser.add_argument('item', metavar='I', type=str, nargs='+', help='playlist or folder location')
	parser.add_argument("-s", "--shuffle", action='store_true')
	parser.add_argument("-l", "--log", help="file to write log to")
	parser.add_argument("--debug", action='store_true', default=False)
	args = parser.parse_args()

	return args

def setup_logging(args):
	""" Everything required when the application is first initialized
	"""

	basepath = os.path.abspath(".")

	# set up all the logging stuff
	LOG_FILENAME = os.path.join(basepath, "%s.log" % __program__)

	# If the log file is specified on the command line then override the default
	if args.log:
		LOG_FILENAME = "%s.log" % args.log

	if args.debug:
		LOG_LEVEL = logging.DEBUG
	else:
		LOG_LEVEL = logging.INFO  # Could be e.g. "DEBUG" or "WARNING"

	# Configure logging to log to a file, making a new file at midnight and keeping the last 3 day's data
	# Give the logger a unique name (good practice)
	log = logging.getLogger(__name__)
	# Set the log level to LOG_LEVEL
	log.setLevel(LOG_LEVEL)
	# Make a handler that writes to a file, making a new file at midnight and keeping 3 backups
	handler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="midnight", backupCount=3)
	# Format each log message like this
	formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
	# Attach the formatter to the handler
	handler.setFormatter(formatter)
	# Attach the handler to the logger
	log.addHandler(handler)  

def main(raw_args):
	""" Main entry point for the script.
	"""

	# call function to parse command line arguments
	args = parse_args(raw_args)
	
	# setup logging
	setup_logging(args)
	
	# connect to the logger we set up
	log = logging.getLogger(__name__)

	# read in our config file
	cfg.read(cfg.__file__)

	# log that we're up and running
	log.debug('initialized')
	
	# this is the rfid reader
	dev = InputDevice(cfg.config['System']['rfidreader'])

	# grab the rfid reader device
	dev.grab()

	cardnumber = []

	if args.item.find(cfg.config['Paths']['playlist']) > -1:
		item_type = "playlist"
	elif args.item.find(cfg.config['Paths']['music']) > -1:
		item_type = "folder"
	else:
		print("%s is in neither the music or playlist paths" % args.item)
		sys.exit( 1 ) 

	print("Swipe the card you wish to assign to item: %s" % args.item)

	db = sqlite3.connect(cfg.config['System']['database'])
	c = db.cursor()

	# wait for events from the rfid reader
	for event in dev.read_loop():
		# if we get a "key pressed down" event
		if event.type == ecodes.EV_KEY and event.value == 1:
			# if it is the enter key we've hit the end of a card number
			if event.code == 28:
				# merge the list in to a string
				card = ''.join(str(num) for num in cardnumber)

				# add (or update) the entry 
				query = "INSERT OR REPLACE INTO Cards (cardnum, item, type, shuffle) values (%s, %s, %s, %s)" % (card, args.item, item_type, args.shuffle)
				c.execute(query)
				db.commit()

				# let the user know we're all good
				print("Assigned card {cardnum} playlist {pl}".format(cardnum=card, pl=args.item))
				# we're done so break out
				break
			else:
				# the event code is 1 more than the actual number key
				number = event.code - 1
				# except for event id 10, which is actually KP_0
				if number == 10:
					number = 0
				# stick the number onto the end of our list
				cardnumber.append(number)

	db.close()   # close db file

if __name__ == '__main__':
	sys.exit(main(sys.argv))
