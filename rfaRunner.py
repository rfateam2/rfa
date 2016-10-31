'''
Created on Oct 19, 2016


@author: sashaalexander
@author: team X
'''
from rfaUtils import getLog,qaPrint,getTestCases
import sys

trid = -1
for arg in sys.argv:    
    if arg.lower().find("--testrun=") > -1:
        trid = int(arg.split("=")[1])
        
test_cases = getTestCases(trid)
if test_cases == -1:
    sys.exit("could not read test run file")

# get the log file handle
log = getLog()
 
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