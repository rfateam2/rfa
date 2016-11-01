'''
Created on Oct 19, 2016


@author: sashaalexander
@author: team 2
@author: korvinca
'''

import sys
import os
from rfaUtils import getLog, qaPrint, getTestCases, getLocalEnv


trid = 0
sc_name = ""
local_dir = os.path.dirname(os.path.realpath(__file__))
# get arguments
for arg in sys.argv:
    if "testrun" in arg.lower():
        # get test suite number
        trid = arg.split("=")[1]
    else:
        # get file name
        sc_name = arg.split(".")[0]
    # print trid, sc_name #optional

# get path to testrun_id file
trid = "/".join([local_dir, trid]) + ".txt"

# get path for local.properties file
loc_prop_file =str("/".join([local_dir, "local.properties"]))

# get local.properties environment in dictionary
prop_dict = getLocalEnv(loc_prop_file)
if prop_dict == -1:
    print "Unable to crate the dictionary with local properties."
    sys.exit("Unable to get local properties.")
else:
    # get folder name for log files
    log_dir_name = prop_dict['log_dir']

# get the log file handle
log = getLog(log_dir_name, sc_name)
# exit if log creation failed
if log == -1:
    sys.exit("Unable to create log file")

# get test cases into the dictionary
test_cases = getTestCases(trid)
# exit if got the errors with creating dictionary
if test_cases == -1:
    qaPrint(log, test_cases)
    sys.exit("Unable to get test cases.")
else:
    qaPrint(log, str(test_cases)) # optional

# close the log file if it is opened
if not log.closed:
    log.close()
