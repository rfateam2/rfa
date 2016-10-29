'''
RFA
Created on Oct 20, 2016

<<<<<<< HEAD
@author: korvinca, group2
=======
@author: sashaalexander
@author: team 2
>>>>>>> 3b50d7a0182bd58deb381826d4f8d44c4399abdc
'''
from datetime import datetime
import os


<<<<<<< HEAD
import os
import datetime
import time
import logging
import sys


def getlog(log_name=None, log_dir=None):
    """ Create log file:
    - with name "testrun" if log_name is None
    - in the local directory if log_dir is None
    """
    if not log_name:
        log_name = "testrun"

    if not log_dir:
        log_dir = 'logs'

    dir_create(log_dir)

    try:
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        hdlr = logging.FileHandler(os.path.join(log_dir + '/' + log_name + "_%s.log"
                                                % str(get_cur_time(sec=True))))
        formatter = logging.Formatter('%(asctime)s %(filename)s '
                                      '[LINE %(lineno)d] %(levelname)s: '
                                      '%(message)s')
        hdlr.setFormatter(formatter)
        log.addHandler(hdlr)
        handler_stream = logging.StreamHandler()
        handler_stream.setLevel(logging.INFO)
        handler_stream.setFormatter(formatter)
        log.addHandler(handler_stream)
    except OSError as err:
        print err
        return -1
    return log

def get_cur_time(sec=None):
    """ Return time stamp as string
    """
    if not sec:
        time_str = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M')
    else:
        # with seconds
        time_str = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
    return time_str

def dir_create(dirname):
    """ Create a new directory
    """
    if not os.path.isdir(dirname):
        try:
            os.makedirs(dirname)
        except OSError as err:
            print err
            return sys.exit(1)

def qaprint(log, message):
    """ Print message with INFO level in the log file and console
    """
    log.info(message)
=======
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


def getCurTime(date_time_format):
    """
    Returns current date_time as a string formatted according to date_time_format
    """
    date_time = datetime.now().strftime(date_time_format)
    return date_time
>>>>>>> 3b50d7a0182bd58deb381826d4f8d44c4399abdc
