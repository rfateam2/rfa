'''
RFA
Created on Oct 20, 2016

@author: korvinca, group2
'''
import os
import datetime
import time
import logging


def getlog(log_name=None, logdir=None):
    """ Create log file in the LOG_DIR if it is presented or local work directory
    """
    if not log_name:
        log_name = "testrun"
    log_dir = logdir  or '.'
    try:
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        hdlr = logging.FileHandler(os.path.join(log_dir + '/' + log_name + "_%s.log"
                                                % str(get_cur_time())))
        formatter = logging.Formatter('%(filename)s %(asctime)s'
                                      '[LINE %(lineno)d] %(levelname)s: %(message)s')
        hdlr.setFormatter(formatter)
        log.addHandler(hdlr)
        handler_stream = logging.StreamHandler()
        handler_stream.setFormatter(formatter)
        handler_stream.setLevel(logging.INFO)
        log.addHandler(handler_stream)
    except OSError as err:
        print err
        return -1
    return log

def get_cur_time(sec=None):
    """ return int timestamps
    """
    if not sec:
        time_str = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M')
    else:
        # optional and can be removed
        time_str = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H%M%S')
    return time_str

def qaprint(message):
    """ Print message in log file and console.
    - doesn't print name of file
    - doesn't print log level
    - doesn't print log name
    """
    log = getlog()
    log.info(message)
