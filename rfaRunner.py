'''
Created on Oct 19, 2016


@author: sashaalexander
@author: nixer (team#2)
'''
from rfaUtils import getLog, qaPrint, getTestCases, getLocalEnv, checkArgv, getDbCursor, getDbConnection, buildURL
import sys

trid = checkArgv(sys.argv)
if trid == -1:
    sys.exit("Unable to process command-line arguments")

loc_prop = getLocalEnv('local.properties')
log_dir = loc_prop['log_dir']

# get the log file handle
log = getLog(log_dir, trid["--testrun"])

# exit if log creation failed
if log == -1:
    sys.exit("Unable to create log file")

message = "It is working, right?"

# get list of test_cases
test_cases = getTestCases(trid["--testrun"])

if test_cases[0] == -1:    
    qaPrint(log, str(test_cases[1]))
    sys.exit("Unable to get test cases from txt file: {}".format(test_cases[1]))

# call qaPrint to print a message with timestamp and write it to the log file
qaPrint(log, message)
qaPrint(log, "Me like what me see")

# close the log file if it open
if not log.closed:
    log.close()