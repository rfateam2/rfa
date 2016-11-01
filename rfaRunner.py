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
        arg1 = arg.split("=")
        trid = arg1[1]
    else:
        arg0 = arg.split(".")
        sc_name = arg0[0]
    # print sc_name, trid

# get path to testrun_id file
trid = "/".join([local_dir, trid]) + ".txt"

# get path for log's directory
loc_prop_file =str("/".join([local_dir, "local.properties"]))
prop_dict = getLocalEnv(loc_prop_file)
if prop_dict == -1:
    print "Unable to crate the dictionary with local properties."
    sys.exit("Unable to get local properties.")
else:
    log_dir_name = prop_dict['log_dir']

# get the log file handle
log = getLog(log_dir_name, sc_name)
# exit if log creation failed
if log == -1:
    sys.exit("Unable to create log file")

# get test cases into the dictionary
test_cases = getTestCases(trid)
# exit if errors is with creating dictionary
if test_cases == -1:
    qaPrint(log, "Something wrong with TC's dictionary.")
    sys.exit("Unable to get test cases.")
else:
    qaPrint(log, str(test_cases)) # optional

# close the log file if it is opened
if not log.closed:
    log.close()
