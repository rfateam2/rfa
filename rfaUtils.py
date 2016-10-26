'''
Created on Oct 20, 2016

@author: nixer (team#2)
'''
import os
import datetime
import sys

def get_cur_time():
    #get today time and format it
    today = datetime.datetime.now()
    time_stamp = today.strftime('%Y%m%d_%H:%M')
    return time_stamp

def create_dir(dir_path):
    #if logs directory does not exist -> create it
    if not os.path.exists(dir_path):
        try:    
            os.makedirs(dir_path)
        except OSError as er:
            print er
            sys.exit(1)

def get_log():
    try:
        #variables for directory path, time stamp and file name
        dir_path = os.path.dirname(os.path.realpath(__file__))+'/logs/'
        create_dir(dir_path)
        time_stamp = get_cur_time()
        file_name = dir_path + "testrun_" + time_stamp + ".log"
        log = open(file_name, 'a') #create and open log in append mode
        return log

    except OSError as er:
        print er
        return -1

def qa_print(log, string):
    print string #pass string to screen
    log.write(string + '\n') #pass string to log file

def close_log(log):
    #if log file exists -> close it
    if os.path.isfile(log.name):
        try:
            log.close()
        except OSError as er:
            print er
            sys.exit(1)
