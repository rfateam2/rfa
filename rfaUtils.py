'''
Created on Oct 19, 2016

@author: sashaalexander
@author: team 2
'''
from datetime import datetime
import os

def getLog(logdir, trid):
    """
    Creates 'logs' directory, if it doesn't exist,
    creates or opens a log file in 'logs' directory.
    """
    # assign a current working directory + '/logs' to log_dir variable (platform independent)
    log_dir = os.path.join(os.getcwd(), logdir)
    # or --> script directory: log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    # or --> user directory: log_dir = os.path.join(os.path.expanduser("~"), "logs")

    try:
        # if logs directory(!) doesn't exist, create it
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        # open log file with prefix and timestamp (platform independent) in Append mode
        log = open(os.path.join(log_dir, "rfaRunner_" + trid + "_" + getCurTime("%Y%m%d_%H-%M") + ".log"), "a")
        return log
    except (OSError, IOError):
        # return -1 in case of exception
        return -1


def qaPrint(log, message):
    """
    Prints 'timestamp + message' to console and writes it to the log file
    """
    # current date and time as string + message. example: [Oct 25 01:52:33.000001] TC1 - Passed
    log_message = getCurTime("[%b %d %H:%M:%S.%f]") + " " + message
    # prints log_message
    print log_message
    # writes message to a log file
    log.write(log_message + "\n")


def getCurTime(date_time_format):
    """
    Returns current date_time as a string formatted according to date_time_format
    """
    date_time = datetime.now().strftime(date_time_format)
    return date_time


def getLocalEnv(loc_prop_file):
    '''
    Reads the content of loc_prop_file to dictionary and returns it 
    '''
    loc_prop = {}
    try:
        with open(loc_prop_file) as f:
            for line in f:
               (key, val) = line.split('=')
               loc_prop[key] = val.strip()
        return loc_prop
    except (OSError, IOError):
        # return -1 in case of exception
        return -1

def getTestCases(trid):    
    keys = ('rest_URL', 'HTTP_method', 'HTTP_RC_desired', 'param_list')
#   keys = ('tcid','rest_URL', 'HTTP_method', 'HTTP_RC_desired', 'param_list')
    test_cases = {}
    try:
        with open(trid+".txt") as f:
            tc_list = f.readlines()
        for i in range(0, len(tc_list)):
            tc = tc_list[i].split("|")                    
            dictionary = dict(zip(keys, map(str.strip, tc[1:])))
            test_cases[tc[0]] = dictionary      
        return test_cases
    except (OSError, IOError):
        # return -1 in case of exception
        return -1