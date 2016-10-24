'''
RFA
Created on Oct 20, 2016

@author: korvinca, group2
'''

import os
import datetime
import time
import logging


def getlog(log_name=None, log_dir=None):
    """ Create log file in the log_dir
    """
    if not log_name:
        log_name = "testrun"
    if not log_dir:
        log_dir = '.'
    else:
        dir_create(log_dir)
    try:
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        hdlr = logging.FileHandler((os.path.join(log_dir + '/' + log_name)
                                    (+ "_%s.log" % str(get_cur_time()))))
        formatter = logging.Formatter('%(asctime)s % (filename)s'
                                      '[LINE %(lineno)d] %(levelname)s:'
                                      ' %(message)s')
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

def dir_create(dirname):
    """ Create a new directory
    """
    if not os.path.isdir(dirname):
        os.makedirs(dirname)

def get_cur_time():
    """ return int timestamps
    """
    time_str = datetime.datetime.fromtimestamp(
        time.time()).strftime('%Y%m%d_%H%M')
    return time_str

def qaprint(message):
    """ Print message in log file and console.
    """
    log = getlog()
    log.info(message)
