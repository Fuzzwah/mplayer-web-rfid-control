# MPlayer Web and RFID Control

A Python based HTTP server which passes commands to mplayer from a 
website or via RFID swipe cards.

## Purpose

In my lounge I have a Raspberry Pi set up with speakers, an RFID 
swipe card reader and an external hard drive. On a magnetic board 
I have a collection of RFID cards that I have printed images 
(generally of album covers) and stuck magnets onto. Each of these
cards is assigned to either a m3u playlist or directly to a 
directory of mp3s. When a card is swiped playback of the associated
music is triggered.

## Installation

1. Install Raspbian Wheezy on your Raspberry Pi model B

        http://www.raspberrypi.org/documentation/installation/installing-images/README.md
        
        Once you have Raspbian up and running, you'll need to log into your R-Pi via SSH 
        as the 'pi' user and complete the following.
        
2. Install all the required packages

        sudo apt-get install mplayer python-setuptools python-pip python-dev build-essential evtest
        sudo easy_install tornado
        sudo pip install --upgrade pip 
        sudo pip install --upgrade virtualenv 
        sudo pip install --upgrade evdev
        
3. Download and extract RFID Music files

        wget https://github.com/Fuzzwah/rfid-music/archive/master.zip
        unzip rfid-music-master.zip
        mv rfid-music-master rfid-music
   
4. Configure a few things, open each of the following files in a text editor and find the config section to get things set up:

        nano mplayer-web-rfid-control
        nano conf.py

5. If you want to run the system as a service do the following:
        
        sudo cp mplayer-web-rfid-control /etc/init.d/
        sudo chmod 755 /etc/init.d/mplayer-web-rfid-control
        sudo update-rc.d mplayer-web-rfid-control defaults

6. Assign playlists or folders to cards using `addcard.py` (use the --shuffle option if you want it to shuffle)

        cd ~/rfid-music
        python addcard.py /home/pi/playlists/PlayListFile.m3u
        (you will be prompted to swipe the card you want to assign it to)
        python addcard.py /media/music/Some\ Band\ -\ Album
        (swipe the card you want to assign it to)
        python addcard.py --shuffle /home/pi/playlists/HugePartyMix.m3u
        (swipe the card you want to assign it to)

## Usage

1. navigate to `http://[machine ip]:8080` to use the remote web menu
2. swipe an rfid card to trigger playback

## Dependencies

- [Python 2.7](http://python.org/download/releases/2.7/)
- [mplayer](http://www.mplayerhq.hu/design7/news.html)
- Python [tornado](http://www.tornadoweb.org/) module
