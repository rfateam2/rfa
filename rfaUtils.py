'''
Created on Oct 19, 2016

@author: sashaalexander
@author: team 2
@author: korvinca
'''
from datetime import datetime
import os


def getTestCases(trid):
    """
    Function will read corresponding id.txt file.
    Function will return that dictionary or -1 in case of error and will try to explain the reason.
    """
    try:
        handle = open(trid)
    except IOError as err:
        return -1, "Failed to open file with error: %s" % err
    else:
        # can be accepted by argument or changed here to change the value to integer
        req_keys = ["rest_URL", "HTTP_method", "HTTP_RC_desired", "param_list"]
        res_suite = dict()
        count = 0
        for line in handle:
            line = line.rstrip()
            if len(line) < 1: continue
            req_values = line.split("|")
            test_num = int(req_values[0])
            # get list of values w/o value of key "tcid"
            req_values = req_values[1:]
            # merge to dictionaries
            one_test = dict(zip(req_keys, req_values))
            try:
                # Change type of the value
                # Better to do it here after merge dictionaries, make the function more universal
                if "HTTP_RC_desired" in one_test:
                    # change value to integer if the key is "HTTP_RC_desired"
                    try:
                        one_test["HTTP_RC_desired"] = int(one_test["HTTP_RC_desired"])
                    except ValueError as err:
                        return -1, err
                if "param_list" in one_test:
                    # change value to list if the key is "param_list"
                    one_test["param_list"] = one_test["param_list"].split(",")
                count += 1
            except ValueError as err:
                return -1, err
            # append sub-dictionaries with test to result
            res_suite[test_num] = one_test
        if len(res_suite) != count or len(res_suite) < 1:
            return -1, "Tests Cases dictionary doesn't mapping with input items."
        return res_suite

def getLocalEnv(prop_file):
    """
    Read the content of the file, and return a dictionary,
    where 1 value of the file becomes key and second value becomes a value.
    """
    prop_set = dict()
    # list key's for change value to integer
    list_for_int = ["debug_mode", 'test_server_port', 'test_db_port', 'verbose_log_mode']
    try:
        handle = open(prop_file)
    except IOError as err:
        print "Failed to open file with error:", err
        return -1
    else:
        count = 0
        for line in handle:
            line = line.rstrip()
            if len(line) < 1: continue
            req_values = line.split("=")
            try:
                if req_values[0] in list_for_int:
                    # change the value to integer if the key exist in the list "list_for_int"
                    try:
                        req_values[1] = int(req_values[1])
                    except ValueError as err:
                        print "Filed to change type of the value in local.parametrs:", err
                        return -1
                # append pair in dictionary
                prop_set[req_values[0]] = req_values[1]
                count += 1
            except OSError as err:
                print "Error with creating Local Environment dictionary:", err
                return -1
        if len(prop_set) != count  or len(prop_set) < 1:
            print "Local Environment dictionary doesn't mapping with input items."
            return -1
    return prop_set


def getLog(log_dir_name, sc_name):
    """
    Creates 'logs' directory, if it doesn't exist, creates or opens a log file in 'logs' directory.
    """
    # assign a current working directory + '/logs' to log_dir variable (platform independent)
    log_dir = os.path.join(os.getcwd(), log_dir_name)
    # or --> script directory: log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    # or --> user directory: log_dir = os.path.join(os.path.expanduser("~"), "logs")

    try:
        # if logs directory(!) doesn't exist, create it
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        # open log file with prefix and timestamp (platform independent) in Append mode
        log = open(os.path.join(log_dir, sc_name + "_" + getCurTime("%Y%m%d_%H-%M") + ".log"), "a")
        return log
    except (OSError, IOError) as err:
        # return -1 in case of exception
        print "Failed to create log: %s" % err
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
