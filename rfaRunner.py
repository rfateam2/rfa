'''
Created on Oct 19, 2016

@author: sashaalexander
@author: georgy.stepiko
'''
from rfaUtils import getLog, qaPrint, dropFile, getTridFullPath, getLocalEnv
import os
import sys

#declaration section
tRun = '--testrun'#mandatory --testrun argument hardcoded - defines testrun ID
mrProper = os.path.dirname(os.path.realpath(__file__)) +'/local.properties'#local.properties hardcoded
mndtr = ['log_dir']#list defines mandatory properties to check them in local.properties file
locProp = getLocalEnv(mrProper, mndtr)#generate dictionary of local properties. all the checks are included.

#kick-off check section
if len(sys.argv) <> 2:#we expect the only argument set an (for a while?)
    sys.exit('CRIT: syntax error. \'--testrun=%trid%\' argument is mandatory ')#--testrun argument is mandatory
else:
    fileToGo = getTridFullPath(sys.argv, tRun)#take tRun argument from arguments list

#func section
log = getLog(fileToGo, locProp['log_dir'])
message = "It is working, right?"#debug message
qaPrint(log, message)#is-log-good check is in qaPrint to let us PRINT message if unable to WRITE
dropFile(log)#tries to close file set if opened. all the checks are implemented in dropFile
