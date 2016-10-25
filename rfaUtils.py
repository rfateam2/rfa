'''
Created on Oct 25, 2016

@author: SalamatB
'''

import os
import datetime

def curTime():
  time = datetime.datetime.now()
  timeNow = time.strftime('_%Y%m%d_%H:%M')
  return timeNow

def getLog():
  try: 
    timeStamp = curTime()
    path = '/Users/...'
    runFile = 'testrun' + timeStamp + '.log'
    log = open(runFile, 'a')
    return log
  except:
    return -1

def qaprint(log, message):
    print message
    log.write(message + '\n')
    log.close()

