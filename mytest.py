'''
Created on Oct 19, 2016

Create a new python module, called mytest.py and write all test code (calls etc) for these functions
Use a mySQL DB and local apache server for all

@author: sashaalexander
@author: korvinca (team#2)
'''
import sys
from rfaUtils import (getLocalEnv, getDbConnection, getDbCursor, queryDb, checkEnv, buildURL,
                      getHttpResponse, getHttpResponseCode)


# read properties
localProperties = getLocalEnv('local.properties')
if localProperties == -1:
    sys.exit('[ERROR]Could not read properties')

# init properties
server_url = localProperties['test_server_URL']
server_port = localProperties['test_server_port']
db_name = localProperties["db_name"]
db_port = localProperties['test_db_port']
db_user = localProperties['db_user']
db_pass = localProperties['db_pass']
list_str = [server_url + "/", "/auth/whoami/", ""]
method = 'get'
method_list = ["Get", "post", "HedD", "DELETE", "OPTIONS", "PUT", "PATCH"]
parameters = {"username": "user_name", "password": "user_password"}

# check env.
check_env = checkEnv(server_url)
if check_env == -1:
    sys.exit("[ERROR] Connection to server failed")

# get connector
connector = getDbConnection(server_url, db_name, db_user, db_pass)
if connector == -1:
    sys.exit("[ERROR] Connection to DB failed")
else:
    print('Connected to MySQL database')
# get cursor
cursor = getDbCursor(connector)
if cursor == -1:
    sys.exit(-1)
else:
    # select something from db
    print "DB query. List of products in table products"
    queryDb(cursor, "SELECT * FROM products")
    # close cursor
    cursor.close()

# close connection
if connector.is_connected:
    connector.close()

# get response
url = buildURL(list_str)
if server_port == "80":
    url = "http://" + url
elif server_port == "443":
    url = "https://" + url
else:
    print "We support only '80' and '443' ports now"
    sys.exit(-1)

# single method test
response = getHttpResponse(url, method, parameters)
print "URL:", response.url
if response == -1:
    sys.exit("[ERROR] Getting response from URL failed")

# tests for the list of methods
for m in method_list:
    response = getHttpResponse(url, method, parameters)
    print "Test list of methods:", m, response
    if response == -1:
        sys.exit("[ERROR] Getting response from URL failed")

# get response code
stringCode = getHttpResponseCode(response, 'string')
if stringCode == -1:
    sys.exit("[ERROR] Getting stringCode failed")
print "Test code 'string':", response, stringCode, type(stringCode)
intCode = getHttpResponseCode(response, 'int')
if stringCode == -1:
    sys.exit("[ERROR] Getting stringCode failed")
print "Test code 'integer':", response, stringCode, type(intCode)
