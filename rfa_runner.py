'''
RAF
Created on Oct 20, 2016

@author: korvinca, group2
'''

from rfa_utils import getlog

def printlog():
    """ Print the message in log folder
    """
    message = "It is working, right?"
    LOG.info(message)

if __name__ == '__main__':
    LOG = getlog()
    printlog()
