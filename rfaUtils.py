"""
Created on Oct 23, 2016

<<<<<<< HEAD
@author: skiftestdqa
"""
import time
import os

def getCurTime():
    # get current time and store as string
    timestr = time.strftime("_%Y%m%d_%H:%M")
    return timestr
=======
@author: sashaalexander
@author: team 2
'''
from datetime import datetime
import os


def getLog():
    """
    Creates 'logs' directory, if it doesn't exist,
    creates or opens a log file in 'logs' directory.
    """
    # assign a current working directory + '/logs' to log_dir variable (platform independent)
    log_dir = os.path.join(os.getcwd(), "logs")
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
>>>>>>> origin/trunk

def getLog():
    try:
        # create directory named "logs"
        log_dir = "logs"
        # create file name
        timestr = getCurTime()
        filename = "testrun" + timestr + ".log"
        # create full path
        full_name = os.path.join(log_dir,filename)
        # open file in append mode
        log = open(full_name, "a")
        return log
    except:
        return -1

<<<<<<< HEAD
def qaprint(log,string):
    # print string to console
    print string
    # write to file and go to new line
    log.write(string + "\n")
=======
def getCurTime(date_time_format):
    """
    Returns current date_time as a string formatted according to date_time_format
    """
    date_time = datetime.now().strftime(date_time_format)
    return date_time
>>>>>>> origin/trunk
