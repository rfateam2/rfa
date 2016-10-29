'''
RAF
Created on Oct 20, 2016

<<<<<<< HEAD
@author: korvinca, group2
'''

from rfaUtils import getlog

def printlog():
    """ Print the message
    """
    log = getlog()
    message = "It is working, right?"
    log.info(message)
    #qaprint(log, message)


if __name__ == '__main__':
    printlog()
=======

@author: sashaalexander
@author: team 2
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
>>>>>>> 3b50d7a0182bd58deb381826d4f8d44c4399abdc
