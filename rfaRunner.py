'''
Created on Oct 19, 2016

@author: sashaalexander
@author: georgy.stepiko
'''
from rfaUtils import getLog,qaPrint, dropLog  # @UnresolvedImport

log = getLog()
message = "It is working, right?"
qaPrint(log,message)
dropLog(log)
