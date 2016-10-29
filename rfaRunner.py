'''
Created on Oct 19, 2016


@author: sashaalexander
@author: team 2
'''
from rfaUtils import getLog, qaPrint, getLocalEnv, getTestCases
import sys

# processing of command-line arguments
args = sys.argv[1].lower().split('=')
if args[0] == '--testrun':
    trid = args[1]
else:
    sys.exit('rfaRunner.py --testrun=<trid>')  

# get list of test_cases
test_cases = getTestCases(trid)

loc_prop = getLocalEnv('local.properties')
log_dir = loc_prop['log_dir']

# get the log file handle
log = getLog(log_dir, trid)

# exit if log creation failed
if log == -1:
    sys.exit("Unable to create log file")

message = "It is working, right?"

# call qaPrint to print a message with timestamp and write it to the log file
qaPrint(log, message)
qaPrint(log, "Me like what me see")

# close the log file if it open
if not log.closed:
    log.close()
