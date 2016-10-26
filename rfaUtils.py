'''
Created on Oct 20, 2016

@author: nixer, korvinca (team#2)
'''
import os
import datetime
import sys

def get_cur_time(sec=None):
    """ Return time stamp as string
    """
    #get today time and format it
    today = datetime.datetime.now()
    if sec:
        time_stamp = today.strftime('%Y%m%d_%H:%M:%S')
    else:
        time_stamp = today.strftime('%Y%m%d_%H:%M')
    return time_stamp

def create_dir(dir_path):
    """ Create a new directory
    """
    #if logs directory does not exist -> create it
    if not os.path.exists(dir_path):
        try:    
            os.makedirs(dir_path)
        except OSError as err:
            print err
            sys.exit(1)

def get_log(log_dir=None, log_name=None):
    """ creates a log file and returns file handler
    """
    if not log_dir:
        log_dir = 'logs'
    if not log_name:
        log_name = "testrun"
        
    #variables for directory path, time stamp and file name
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/' + log_dir
    create_dir(dir_path)
    time_stamp = get_cur_time()
    file_name = dir_path + "/" + log_name + "_" + time_stamp + ".log"
    try:
        log = open(file_name, 'a') #create and open log in append mode
        return log
    except OSError as err:
        print err
        return -1

def qa_print(log, string):
    """ prints message and writs message to the log file
    """
    time_stamp = get_cur_time(sec=True)
    print time_stamp + ' ' + string #pass string to screen
    log.write(time_stamp + ' ' + string + '\n') #pass string to log file

def close_log(log):
    """ Close the log file
    """
    #if log file exists -> close it
    if os.path.isfile(log.name):
        try:
            log.close()
        except OSError as err:
            print err
