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
    """ Create log file:
    - with name "testrun" if log_name is None
    - in the local directory if log_dir is None
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
        hdlr = logging.FileHandler(os.path.join(log_dir + '/' + log_name + "_%s.log"
                                                % str(get_cur_time())))
        formatter = logging.Formatter('%(asctime)s %(filename)s '
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

def get_cur_time():
    """ Return timestamp
    """
    time_str = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d_%H:%M')
    return time_str

def dir_create(dirname):
    """ Create a new directory
    """
    if not os.path.isdir(dirname):
        os.makedirs(dirname)

def qaprint(log, message):
    """ Print message with INFO level in the log file and console
    """
    log.info(message)
