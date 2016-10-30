'''
Created on Oct 23, 2016

<<<<<<< HEAD
@author: skiftestqa
'''
from RAF_CODE_01.rfaUtils import getLog,qaprint
=======

@author: sashaalexander
@author: team 2
'''
from rfaUtils import getLog,qaPrint

import sys
>>>>>>> origin/trunk

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
