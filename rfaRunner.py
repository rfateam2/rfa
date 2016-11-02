'''
Created on Oct 19, 2016


@author: sashaalexander
@author: team 2
'''

import sys
import os
from rfaUtils import getLog, qaPrint, getTestCases, getLocalEnv, checkArgv

local_dir = os.path.dirname(os.path.realpath(__file__))

# If we want to use any arguments with "=" in rfaRunner
#arg_dict = checkArgv(sys.argv)
#sc_name =arg_dict["file_name"]
#trid_int = arg_dict["--testrun"]
#print str(arg_dict)
#print sc_name, trid_int

# get arguments here with argv
for arg in sys.argv:
    if "testrun" in arg.lower():
        # get test suite number
        trid_int = int(arg.split("=")[1])
        if trid_int not in range(10001):
            sys.exit("ERROR: The number of testcase %d is out of range 0-10000." % trid_int)
    else:
        # get file name
        sc_name = arg.split(".")[0]
    #print trid, sc_name #optional

# get path to testrun_id file
trid = "/".join([local_dir, str(trid_int)]) + ".txt"

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
log = getLog(log_dir_name, sc_name)
# exit if log creation failed
if log == -1:
    sys.exit("ERROR: Unable to create log file")

# get test cases into the dictionary
test_cases = getTestCases(trid)
# exit if got the errors with creating dictionary
if test_cases == -1:
    qaPrint(log, test_cases)
    sys.exit("ERROR: Unable to get test cases.")
else:
    qaPrint(log, str(test_cases)) # optional

# close the log file if it is opened
if not log.closed:
    log.close()
