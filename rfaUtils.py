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
    
    file_name = 'testrun_' + getCurTime().strftime('%Y%m%d_%H:%M') + '.log'
    full_path = os.path.join(directory, file_name)
    
    return open(full_path, 'a')


def qaprint(log, message):    
    msg = getCurTime().strftime('%Y-%m-%d %H:%M:%S') + ' - ' + message
    print msg
    log.write(msg + '\n')


def getCurTime():
    return datetime.datetime.utcnow()