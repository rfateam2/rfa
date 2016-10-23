'''
RAF
Created on Oct 20, 2016

@author: korvinca, group2
'''

from rfa_utils import getlog, qaprint

def printlog():
    """ Print the message
    """
    test_name = 'assignment_01'
    log = getlog(test_name)
    message = "It is working, right?"
    log.info(message)
    log.error(message)


def printlog_v1():
    """ Print the message var. 1
    """
    message = "It is working, right?"
    qaprint(message)

if __name__ == '__main__':
    printlog()
    printlog_v1()
