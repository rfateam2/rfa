'''
Created on Oct 19, 2016

@author: sashaalexander
@author: team 2
@author: korvinca
'''
from datetime import datetime
import os
import sys


def getTestCases(trid=None):
    """
    Function will read corresponding id.txt file.
    Function will return that dictionary or -1 in case of error
    and will try to explain the reason
    """
    fname = "42.txt"
    try:
        handle = open(fname)
    except:
        raise
        return -1
    req_keys = ["rest_URL", "HTTP_method", "HTTP_RC_desired", "param_list"]
    res_suite = dict()
    for line in handle:
        line = line.rstrip()
        if len(line) < 1 : continue
        req_values = line.split("|")
        test_num = int(req_values[0])
        req_values = req_values[1:]
        one_test = dict(zip(req_keys, req_values))
        res_suite[test_num] = one_test
    if len(res_suite) < 1:
        res_suite = -1
    print res_suite
    return res_suite


    #lst.append(])
#print lst

def getLocalEnv(prop_file):
    """
    Read the content of the file, and return a dictionary,
    where 1 value of the file becomes key and second value becomes a value.
    """
    local_prop = ''
    return local_prop

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

if __name__ == '__main__':
    getTestCases()
