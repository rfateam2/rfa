'''
Created on Oct 19, 2016

@author: sashaalexander
@author: georgy.stepiko
'''
import datetime
import os

# format is testrun_20161020_18:43.log
def getLog():
    try:
        #filename = 'logs/testrun_' + getCurTime() + '.log'
        filepath = os.path.dirname(os.path.realpath(__file__)) +'/logs'
        filename = filepath + '/testrun_' + getCurTime() + '.log'
        if not os.path.isdir(filepath):
            try:
                os.makedirs(filepath)
            except OSError as er:
                print er
                return -1
        print filename
        log = open(filename, 'a')
        return log
    except OSError as er:
        print er
        return -1
    
def dropLog(log):
    try:
        log.close()
    except OSError as er:
        print er
        return -1

def qaPrint(log, line):
    timestamp = getCurTime() 
    log.write( timestamp + ' :: ' + line + '\r\n')#Don't forget about timestamps in logfiles.
    print(line)#finally display text - no timestamp here
    
def getCurTime():
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H:%M') #time format is 20161020_18:43  
    return  timestamp
