'''
Created on Nov 28, 2016


@author: nixer (team#2)
'''
from rfaUtils import getLog, qaPrint, getTestCases, getLocalEnv, checkArgv, getDbCursor, getDbConnection, buildURL
import sys

loc_prop = getLocalEnv('local.properties')
hst = loc_prop['test_server_URL']
db = loc_prop['db_name']
lg = loc_prop['db_user']
pw = loc_prop['db_pass']
str_list = [hst,'/','/files/show_all']

connection = getDbConnection(hst, db, lg, pw)
getDbCursor(connection)
url = buildURL(str_list)