'''
Created on Oct 19, 2016

@author: sashaalexander
'''
import os
import datetime

def getCurTime():
    time = datetime.datetime.now()
    timeNow = time.strftime('_%Y%m%d_%H:%M')
    return timeNow

def getLog():
    try:
        path = os.path.dirname(os.path.realpath(__file__))+'/logs/'
        show_time = getCurTime()
        log_name = path + "testrun_" + show_time + ".log"
        if not os.path.exists(path):
            os.makedirs(path)
        log = open(log_name, 'a')
        return log
    except OSError as er:
        return -1

def qaprint(log, string):    
    print string
    log.write(string + '\n')
    log.close()