'''
Created on Oct 19, 2016

@author: sashaalexander
@author: georgy.stepiko
'''
import datetime
import os

def getLog():
    '''Create log file
    - try to create directory; exceptions are handled;
    - try to open/ create log file under path created
    - return file opened
    -- format is testrun_20161020_18:43.log
    '''
    try:
        #filename = 'logs/testrun_' + getCurTime() + '.log'
        filepath = os.path.dirname(os.path.realpath(__file__)) +'/logs'
        filename = filepath + '/testrun_' + getCurTime() + '.log'
        if not os.path.isdir(filepath):
            try:
                os.makedirs(filepath)
            except OSError as er:
                print 'Unable to create Log file directory. Reason: ' + er
                return -1
        print filename
        log = open(filename, 'a')
        return log
    except OSError as er:
        print 'Unable to create/open Log file. Reason: ' + er
        return -1

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

def getCurTime():
    '''Generate timestamp by format declared.
    '''
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H:%M')#time format is 20161020_18:43
    return  timestamp

def dropLog(smth):
    '''Close log file
    - try to close file if there is something to close
    '''
    if isBad(smth):
        print 'Unable to close file. Reason: Nothing to close'
    else:
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
