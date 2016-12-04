'''
Created on Oct 19, 2016
@author: sashaalexander
@author: team 9
'''

import os
import sys
import requests
import mysql.connector
from datetime import datetime


def getLog(testName, logDir):
    """
    Creates logDir directory, if it doesn't exist,
    creates or opens a log file in 'logs' directory.
    """
    # assign a current working directory + '/logs' to log_dir variable (platform independent)
    log_dir = os.path.join(os.getcwd(), logDir)
    # or --> script directory: log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    # or --> user directory: log_dir = os.path.join(os.path.expanduser("~"), "logs")

    try:
        # if logs directory(!) doesn't exist, create it
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
            # open log file with prefix and timestamp (platform independent) in Append mode
        log = open(os.path.join(log_dir, testName + "_" + getCurTime("%Y%m%d_%H-%M-%S") + ".log"), "a")
        return log
    except (OSError, IOError):
        # return -1 in case of exception
        return -1


def qaPrint(log, message):
    """
    Prints 'timestamp + message' to console and writes it to the log file
    """
    # current date and time as string + message. example: [Oct 25 01:52:33.000001] TC1 - Passed
    log_message = getCurTime("[%b %d %H:%M:%S.%f]") + " " + message
    # prints log_message
    print log_message
    # writes message to a log file
    log.write(log_message + "\n")


def getCurTime(date_time_format):
    """
    Returns current date_time as a string formatted according to date_time_format
    """
    date_time = datetime.now().strftime(date_time_format)
    return date_time


def getLocalEnv(propertiesFileName):
    try:
        properties = open(propertiesFileName, "r")
        props = {}
        for line in properties:
            line = line.strip()
            #skip line without "="
            if "=" not in line: continue
            #skip comments
            if line.startswith("#"): continue
            k, v = line.split("=", 1)
            props[k] = v
        if not properties.closed: properties.close()
        return props
    except Exception as e:
        print e
        if not properties.closed: properties.close()
        return -1


def getTestCases(testRunId,log):
    TEST_CASE_KEYS = ('rest_URL', 'HTTP_method', 'HTTP_RC_desired', 'param_list')
    testCases = {}
    try:
        testCasesFile = open(str(testRunId) + '.txt')
        #loop through lines in file
        for line in testCasesFile:
            line = line.strip()
            #skip empty line
            if line == '': continue
            #skip comments
            if line.startswith("#"): continue
            #convert last element to a list
            tc = line.split("|")
            tc[-1] = tc[-1].split(',')
            if tc[0] not in testCases:
                #fill dict with keys from TEST_CASE_KEYS and slice of list , skipping 1st element - tcid
                testCases[tc[0]] = dict(zip(TEST_CASE_KEYS, tc[1:]))
            else:
                qaPrint(log,"[INFO]Duplicated tcid {}, skipping line".format(tc[0]))
        if not testCasesFile.closed: testCasesFile.close()
        return testCases
    except Exception as ex:
        print ex
        return -1


def usage():
    print ('[ERROR]Invalid parameters. Proper usage: rfaRunner.py --testrun=<testRunId>')


def closeLog(log):
    # close the log file if it open
    if not log.closed:
        qaPrint(log, '[INFO]Test suite ends')
        log.close()


def getArguments(args):
    arguments = {}
    if len(args) < 2:
        sys.exit(usage())
    try:
        arguments['testName'] = args[0].split('/')[-1].replace('.py', '')
        for i in range(1, len(args)):
            arg = args[i].split('=')
            if arg[0].lower() == '--testrun':
                arguments['trid'] = int(arg[1])
                if (arguments['trid'] not in range(1, 10001)):
                    usage()
                    sys.exit("[ERROR]Invalid parameter, value should be [0-10000]")
        return arguments
    except Exception:
        sys.exit(usage())

def getDbConnection(db_url, db_name, db_user, db_pass):
    """
    Function will accept host URL and host credentials
    Function will create a connection to mySQL DB we've installed
    Function will return a connection object in case of success (-1 if not successful)
    NOTE: IT IS totally OK for us to use clear text passwords at this time everywhere
    """
    try:
        conn = mysql.connector.connect(host=db_url,database=db_name,user=db_user,password=db_pass)
        if conn.is_connected():
            print('Connected to MySQL database')
        return conn
    except Exception as err:
        print err.message
        return -1

def getDbCursor(connection):
    """
    Function will accept a connection and return a cursor, if success (-1 if not successful)
    """
    cursor = connection.cursor()
    if _check_db(cursor) != -1:
        return cursor
    else:
        print "[ERROR] Getting cursor failed."
        return -1


def queryDb(cursor, query):
    """
    *Create NO implementation for it yet, unless you're bored*
    """
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print row[1]
    except Exception as err:
        print "[ERROR] Getting cursor failed with error: %s" % err.message
        return -1

def buildURL(list_of_string):
    """
    Function to accept list of string and build URL-looking string, returning it if success.
    (-1 blah blah blah)
    Exam ple:
    Local test server is string 0: "myhost.com"
    REST API Path is string 1: "files/show_all" string 2 is empty: ""
    So, our string to return will be "myhost.com/files/show_all"
    Note that we've put a "/" in string. BUT ONLY if it isn't there already
    (hint: check first and last chars of string)
    """
    if list_of_string[0][-1] is "/":
        list_of_string[0] = list_of_string[0][:-1]
    list_urls = []
    try:
        for x in list_of_string[1:]:
            if x == "": continue
            if x.strip()[0] is "/":
                one_url = list_of_string[0] + x
            else:
                one_url = list_of_string[0] + "/" + x
            list_urls.append(one_url)
        return list_urls
    except Exception as err:
        print err.message
        return -1

def getHttpResponse(url, method, parameters=None):
    """
    This function is to take URL (as string), HTTP Method (as string), and parameters (as dictionary)
    This function is to make HTTP request to URL provided and return a Response as is. (-1 blah blah blah)
    Inside of it, make a multiple code blocks for different HTTP methods: GET, POST, HEAD, DELETE, OPTIONS
    """
    method = method.upper()
    #re.match("GET", method, re.IGNORECASE)
    try:
        if method == 'GET':
            response = requests.get(url, params=parameters)
        elif method == 'POST':
            response = requests.post(url, params=parameters)
        elif method == 'HEAD':
            response = requests.head(url)
        elif method == 'DELETE':
            response = requests.delete(url)
        elif method == 'OPTIONS':
            response = requests.options(url)
        else:
            print ("Unsupported method: %s", method)
            return -1
        return response
    except Exception as err:
        print err.message
        return -1

def getHttpResponseCode(response_object, indicator):
    """
    This function is to take a Response object and indicator (string or int) and returns a response code
    (or it's string representation)
    So, in first case our code is '404', but in second case it is 404
    """
    response_code = response_object.status_code
    if indicator == 'string':
        response_code = str(response_code)
    elif indicator == 'int':
        response_code = int(response_code)
    else:
        print ("Inappropriate indicator: %s. Expected 'string' or 'int'.", indicator)
        return -1
    return response_code

def checkEnv(server_url):
    """ Write no implementation to it, but make it return True """
    try:
        # check server availability
        ping = _check_ping(server_url)
        if ping == -1:
            return -1
        return True
    except Exception as err:
        print err.message
        return -1

def _check_ping(server_URL):
    """ Check server IP or URL availability and return True or -1 """
    response = os.system("ping -c 1 " + server_URL)
    # and then check the response...
    if response == 0:
        return True
    else:
        return -1

def _check_db(cursor):
    """ Check cursor is up """
    try:
        cursor.execute("SELECT VERSION()")
        ver = cursor.fetchone()[0]
        if ver is None:
            return -1
    except:
        return -1
