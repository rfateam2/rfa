'''
Created on Oct 19, 2016


@author: sashaalexander
@author: team 2
'''

import sys
import os
from rfaUtils import getLog, qaPrint, getTestCases, getLocalEnv, checkArgv

local_dir = os.path.dirname(os.path.realpath(__file__))

# Pull arguments from cli to dictionary,split by "="
arg_dict = checkArgv(sys.argv)
if arg_dict == -1:
    sys.exit("ERROR: Unable to crate the dictionary with arguments.")
# print arg_dict # Print dict for check

# get path to testrun_id file
trid = "/".join([local_dir, arg_dict["--testrun"]]) + ".txt"

# get path for local.properties file
loc_prop_file = str("/".join([local_dir, "local.properties"]))

# get local.properties environment in dictionary
prop_dict = getLocalEnv(loc_prop_file)
if prop_dict == -1:
    sys.exit("ERROR: Unable to crate the dictionary with local properties.")
else:
    # get folder name for log files
    log_dir_name = prop_dict['log_dir']

# get the log file handle
log = getLog(log_dir_name, arg_dict["file_name"])
# exit if log creation failed
if log == -1:
    sys.exit("ERROR: Unable to create log file")

# get test cases into the dictionary
test_cases = getTestCases(trid)
if test_cases == -1:
    qaPrint(log, test_cases)
    sys.exit("ERROR: Unable to get test cases from input file.")

# qaPrint(log, str(test_cases)) # Print dict for check

# close the log file if it is opened
if not log.closed:
    log.close()
