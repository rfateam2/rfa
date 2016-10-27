'''
RAF
Created on Oct 20, 2016

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
