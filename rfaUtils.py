'''
Created on Oct 20, 2016

@author: nixer (team#2)
'''
import os, datetime

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
    
        file = open(file_name, 'a') #create and open file in append mode
        return file
    
    except OSError as er:
        print er
        return -1

def qaprint(log, string):
    print string #pass string to screen
    log.write(string + '\n') #pass string to log file
    #log.close()