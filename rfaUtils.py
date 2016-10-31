'''
Created on Oct 19, 2016

@author: sashaalexander
@author: georgy.stepiko
'''
import datetime
import os
import sys

def getLog(tcNum, logDir):
    '''Create log file
    - try to create directory; exceptions are handled;
    - try to open/ create log file under path created
    - return file opened
    -- format is testrun_20161020_18:43.log
    '''
    try:
        filepath = os.path.dirname(os.path.realpath(__file__)) + '/' + logDir
        filename = filepath + '/' + tcNum + '_' + getCurTime() + '.log'
        if not os.path.isdir(filepath):
            try:
                os.makedirs(filepath)
            except OSError as er:
                print 'Unable to create Log file directory. Reason: ' + er
                return -1
        log = open(filename, 'a')
        return log
    except OSError as er:
        print 'Unable to create/open Log file. Reason: ' + er
        return -1

def getLocalEnv(props, mProps):
    '''gets all the values from local.properties (hardcoded) file
    CRITICAL: any error here will cause sys.exit - unable to continue if function failed
    '''
    propDict = {}#local.properties dictionary empty
    if os.path.isfile(props):#local.properties file check
        pass#OK
    else:
        #'local.properties lost' is critical issue - exit
        sys.exit('CRIT: local.properties file is lost. Please verify your setup.')#bye!
    try:
        rawProps = open(props)#try to open local.properties file
    except OSError as er:
        sys.exit('CRIT: unable to open \'local.properties\' file to read. Reason: ' + er)#bye!
    for line in rawProps:#read any line from local.properties
        pairedProps = line.split('=')#make another properties pair (service)
        propDict[pairedProps[0]] = pairedProps[1].strip()#and push pair in dictionary. all the \r\n or \n are stripped sure
    dropFile(rawProps)#close local.propeties (all the opened/exist/... checks included
    for guy in mProps:#(!) take any property from hardcoded mandatory list...
        if guy in propDict:#...and ensure them are in new dictionary created
            pass#OK
        else:
            #exit if any of them is lost
            sys.exit('CRIT: mandatory property \"' + guy + '\" is lost in local.properties file!')
    return propDict#it was long way to return cooked dictionary with all the midair checks passed

def getTridFullPath(guys, tridguy):
    '''get test run ID from the argument lists
    the most of checks are in extArg so here special check only
    '''
    tridNum = extArg(guys, tridguy)#extract --testrun=%value% from arguments list - refer extrArg for details
    if int(tridNum) in range(10001):#make sure it is in 0..10000 range
        pass#OK
    else:
        sys.exit('\'--testrun=%trid%\' argument must be INT value from 0 through 10000!')#trid is out of range or is not INT
    return tridNum


def qaPrint(log, line):
    '''Print log message
    - generate timestamp
    - display message
    - try to write the same message with timestamp in file opened before
    - al lthe errors/exceptions are handled
    '''
    timestamp = getCurTime()
    print line#finally display text - no timestamp here
    if isBad(log):
        print 'Unable to Test Log file for some reasons above.'
        return -1
    else:
        log.write(timestamp + ' :: ' + line + '\r\n')#Don't forget about timestamps in logfiles.

def extArg(guys, guy):
    '''try to extract any (but exact!) argument from arguments list
    I mean we could have extended arguments lis in furture so it will work with any of them
    CRIT: sys exit if argument is not found
    '''
    for t in (0, len(guys)-1):#will seek in arguments list
        things = guys[t].split('=')#no 'lower' option here to do not corrupt argument value @nixer
        if things[0].lower() == guy:#So if we catched the guy...(argument key is case insensitive as requested)
            return things[1]#...we return him
    #if requested (mandatory!) argument is not found - exit, sorry
    sys.exit('CRIT: --testrun=<trid> argument is mandatory but not found!')

def getCurTime():
    '''Generate timestamp by format declared.
    '''
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H:%M')#time format is 20161020_18:43
    return  timestamp

def dropFile(smth):
    '''Close log file
    - try to close file if there is something to close
    '''
    if isBad(smth):
        print 'Unable to close file. Reason: Nothing to close'
    else:
        if not smth.closed:
            try:
                smth.close()
            except OSError as er:
                print 'Unable to close file. Reason: ' + er
                return -1

def isBad(smth):
    '''Contains "%smth% is bad" criteria
    delegated in separate function as soon as criteria may vary or become more complex
    we will be able just to change criteria
    '''
    return bool(smth == -1)
