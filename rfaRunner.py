'''
Created on Oct 19, 2016

@author: sashaalexander
'''
from rfaUtils import get_log, qa_print, close_log

log = get_log()
# (log_file mode, log_file path)
message = "It is working, right?"
loghd = log[0]
qa_print(loghd, message)
close_log(log[1])
