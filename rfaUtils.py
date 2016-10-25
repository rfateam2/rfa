'''
Created on Oct 23, 2016

@author: skiftestdqa
'''

import time
import os

def getCurTime():
    # get current time and store as string
    timestr = time.strftime("_%Y%m%d_%H:%M")
    return timestr

def getLog():
    try:
        # create directory named "logs"        
        log_dir = "logs"
        # create file name
        timestr = getCurTime()
        filename = "testrun" + timestr + ".log"
        # create full path
        full_name = os.path.join(log_dir,filename)
        # open file in append mode
        log = open(full_name, "a")
        return log
    except:
        return -1

def qaprint(log,string):
    # print string to console
    print string
    # write to file and go to new line
    log.write(string + "\n") 
    
    
    