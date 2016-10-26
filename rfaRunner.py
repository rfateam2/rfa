
'''
RAF
Created on Oct 20, 2016
@author: team#2
'''

from rfaUtils import get_log, qa_print, close_log


log = get_log()
# (log_file mode, log_file path)
message = "It is working, right?"
loghd = log[0]
qa_print(loghd, message)
logpath = log[1]
close_log(logpath)