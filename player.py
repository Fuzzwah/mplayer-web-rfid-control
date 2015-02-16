from subprocess import Popen, PIPE, call
from threading import Thread
from Queue import Queue
import os
import util
from main import ServerStatus

try:
    commandQueue ## Global multi-process queue to accept player commands
    playQ        ## Global multi-process queue to accept files to play
except:
    commandQueue = Queue()
    playQ = Queue()

def listen():
    while True:
        aFile = playQ.get()
        if util.isInRoot(aFile):
            ServerStatus.send(util.nameToTitle(aFile), event='playing')
            playerCmd = "mplayer"
            cmdTable = {'step-backward': "\x1B[B", 'backward': "\x1B[D", 'forward': "\x1B[C", 'step-forward': "\x1B[A",
						 ## down | left | right | up
						 'volume-down': "9", 'volume-off': "m", 'volume-up': "0",
						 'stop': "q", 'pause': " ", 'play': " "}
            playFile(playerCmd, aFile, cmdTable)

def playFile(playerCmd, fileName, cmdTable):
    __clearQueue(commandQueue)
    activePlayer = Popen(playerCmd + [fileName], stdin=PIPE)
    while activePlayer.poll() == None:
        try:
            res = commandQueue.get(timeout=1)
            activePlayer.stdin.write(cmdTable[res])
            if unicode(res) == unicode("stop"):
                ServerStatus.send(util.nameToTitle(fileName), event="stopped")
                __clearQueue(playQ)
                activePlayer.terminate()
                return False
        except:
            None
    ServerStatus.send(util.nameToTitle(fileName), event="finished")
    return True
    
def playList(playerCmd, fileName, cmdTable):
    __clearQueue(commandQueue)
    activePlayer = Popen(playerCmd + [fileName], stdin=PIPE)
    while activePlayer.poll() == None:
        try:
            res = commandQueue.get(timeout=1)
            activePlayer.stdin.write(cmdTable[res])
            if unicode(res) == unicode("stop"):
                ServerStatus.send(util.nameToTitle(fileName), event="stopped")
                __clearQueue(playQ)
                activePlayer.terminate()
                return False
        except:
            None
    ServerStatus.send(util.nameToTitle(fileName), event="finished")
    return True    

def __clearQueue(q):
    while not q.empty():
        q.get()
    return True

### Start the player process
playerThread = Thread(target=listen, args=())
playerThread.daemon = True
playerThread.start()
