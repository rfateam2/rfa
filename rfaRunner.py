'''
Created on Oct 19, 2016


@author: sashaalexander
@author: team X
'''
from rfaUtils import getLog,qaPrint

import sys

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
