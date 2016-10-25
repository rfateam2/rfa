'''
Created on Oct 20, 2016

@author: nixer (team#2)
'''
import os
import datetime

def getCurTime():
    #get today time and format it
    today = datetime.datetime.now()
    time_stamp = today.strftime('%Y%m%d_%H:%M')
    return time_stamp

def getLog():
    try:
        #variables for directory path, time stamp and file name
        dir_path = os.path.dirname(os.path.realpath(__file__))+'/logs/'
        time_stamp = getCurTime()
        file_name = dir_path + "testrun_" + time_stamp + ".log"

        #if logs directory does not exist -> create it
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        log = open(file_name, 'a') #create and open log in append mode
        return log

    except OSError as er:
        print er
        return -1

def qaprint(log, string):
    print string #pass string to screen
    log.write(string + '\n') #pass string to log file

def close_log(log):
    log.close()
