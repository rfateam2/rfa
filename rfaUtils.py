'''
RFA
Created on Oct 20, 2016

@author: korvinca, group2
'''

import os
import datetime
import time
import logging
import sys


def getlog(log_name=None, log_dir=None):
    """ Create log file:
    - with name "testrun" if log_name is None
    - in the local directory if log_dir is None
    """
    if not log_name:
        log_name = "testrun"

    if not log_dir:
        log_dir = '.'

    dir_create(log_dir)

    try:
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        hdlr = logging.FileHandler(os.path.join(log_dir + '/' + log_name + "_%s.log"
                                                % str(get_cur_time())))
        formatter = logging.Formatter('%(asctime)s %(filename)s '
                                      '[LINE %(lineno)d] %(levelname)s: '
                                      '%(message)s')
        hdlr.setFormatter(formatter)
        log.addHandler(hdlr)
        handler_stream = logging.StreamHandler()
        handler_stream.setLevel(logging.INFO)
        handler_stream.setFormatter(formatter)
        log.addHandler(handler_stream)
    except OSError as err:
        print err
        return -1
    return log

def get_cur_time(sec=None):
    """ Return time stamp as string
    """
    if not sec:
        time_str = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M')
    else:
        # with seconds
        time_str = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
    return time_str

def dir_create(dirname):
    """ Create a new directory
    """
    if not os.path.isdir(dirname):
        try:
            os.makedirs(dirname)
        except OSError as err:
            print err
            return sys.exit(1)

def qaprint(log, message):
    """ Print message with INFO level in the log file and console
    """
    log.info(message)
