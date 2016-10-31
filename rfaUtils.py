'''
Created on Oct 19, 2016

@author: sashaalexander
@author: team X
'''
from datetime import datetime
import os


def getLog():
    """
    Creates 'logs' directory, if it doesn't exist,
    creates or opens a log file in 'logs' directory.
    """
    # assign a current working directory + '/logs' to log_dir variable (platform independent)
    #log_dir = os.path.join(os.getcwd(), "logs")
    prop_set = getLocalEnv("local.properties")
    log_dir = prop_set["log_dir"]
    
    # or --> script directory: log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    # or --> user directory: log_dir = os.path.join(os.path.expanduser("~"), "logs")

    try:
        # if logs directory(!) doesn't exist, create it
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        # open log file with prefix and timestamp (platform independent) in Append mode
        log = open(os.path.join(log_dir, "rfaRunner_" + getCurTime("%Y%m%d_%H-%M") + ".log"), "a")
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


def getLocalEnv(prop_file):
    try:
        prop_set = {}
        with open(os.path.join(os.getcwd(), "local.properties"), "r") as f:
            for line in f:
                key, value = line.strip("\n").split("=")
                prop_set[key] = value
        return prop_set
    except IOError:
        return -1
    

def getTestCases(trid):
    try:
        res = []
        with open(os.path.join(os.getcwd(), str(trid) + ".txt"), "r") as f:
            for line in f:
                test_case = line.strip("\n").split("|")
                res.append(test_case)
        
        return res
    except IOError:
        return -1