'''
Created on Oct 19, 2016

@author: sashaalexander
'''
import datetime
import os


def getLog():
    directory = '../log'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    fileName = 'testrun_' + getCurTime().strftime('%Y%m%d_%H:%M') + '.log'    
    return open(directory + '/' + fileName, 'w+')


def qaprint(log, message):    
    msg = getCurTime().strftime('%Y-%m-%d %H:%M:%S') + ' - ' + message
    print msg
    log.write(msg + '\n')


def getCurTime():
    return datetime.datetime.utcnow()