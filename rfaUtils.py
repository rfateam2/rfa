'''
Created on Oct 19, 2016

@author: sashaalexander
@author: nixer (team#2)
'''
from datetime import datetime
import os
import sys

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

def checkArgv():
    # processing of command-line arguments
    if len(sys.argv) != 2:
        sys.exit('one argument is required: --testrun=<trid>')
    else:
        args = sys.argv[1].lower().split('=')
        if args[0] == '--testrun' and args[1].isdigit() and len(args) > 1:
            trid = args[1]
            if int(trid) in range(10001):
                pass
            else:
                sys.exit('test run number should be in range [0-10000]')
        else:
            sys.exit('rfaRunner.py --testrun=<trid>')
        return trid

def getLocalEnv(loc_prop_file):
    '''
    Reads the content of loc_prop_file to dictionary and returns it 
    '''
    loc_prop = {}
    try:
        with open(loc_prop_file) as f:
            for line in f:
                try:
                   (key, val) = line.split('=')
                   val = val.strip()
                   if val.isdigit(): # checking if value is digit -> convert to int
                       val = int(val)
                   loc_prop[key] = val
                except ValueError as err:
                    print "Local properties file has wrong format: ", err 
                    return -1
        return loc_prop
    except (OSError, IOError):
        # return -1 in case of exception
        return -1

def getTestCases(trid): 
    '''
    Reads the content of test_run_file to dictionary of dictionaries and returns it 
    '''   
    keys = ('rest_URL', 'HTTP_method', 'HTTP_RC_desired', 'param_list') # key tuple
    test_cases = {}
    try:
        with open(trid+".txt") as f:
            tc_list = f.readlines() # reads each line of test_run_file in list
        for i in range(0, len(tc_list)): 
            tc = tc_list[i].split("|") # split line and create a value list                     
            dictionary = dict(zip(keys, map(str.strip, tc[1:]))) # merge key tuple and value list to dictionary
            param_list = dictionary['param_list'].split(',') # split param_list and create a list
            dictionary['param_list'] = param_list # replace value of param_list by new list
            http_rc = int(dictionary['HTTP_RC_desired']) # convert HTTP_RC_desired value to int
            dictionary['HTTP_RC_desired'] = http_rc # replace value of HTTP_RC_desired by new int value
            test_cases[int(tc[0])] = dictionary # append final dictionary to test_cases dictionary      
        return test_cases
    except (OSError, IOError):
        # return -1 in case of exception
        return -1