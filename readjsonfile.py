#!/usr/bin/env python3
""" 
I took this from my galip project
https://github.com/blindgumption/galip

I stripped out all the inotify stuff,
I only want to be able to read in text, determine if it's JSON 
and print out some of it.

generator that returns objects from files containing lines of text each which is syntactically valid JSON

lazy iterator to get JSON objects from file.
The expectation is each line in the file is syntactically valid JSON.
Lines that are not valid JSON will be ignored.

getJsonObjectsFromFile(filename) will iterate through each line in the file and return an object if the line is valid JSON
"""


import json
import sys 
import os.path as path 

def getFileComponents(name):
    """
    return (apspath, dirname, filename) if name is the name of a file, else throw exception.

    if 'name' is the name of a file, 
    get its absolute path and return that 
    along with the directory the file is in and the filename itself 
    """
    assert path.isfile(name), "input [{}] must be the name of a file".format(name)
    abs = path.abspath(name)
    (dirname, filename) = path.split(abs)
    return (abs, dirname, filename)


def isJson(tstr):
    """ if tstr is valid JSON, return object created from the string, else, return None """ 
    ret = None
    try:
        ret = json.loads(tstr)
    except ValueError:
        pass
    return ret


def getJsonObjectFromLog(binary_log):
    """ take the binary string and return an object if the string is valid JSON """ 
    log = binary_log.decode(errors='ignore')
    return isJson(log)

def getJsonObjectsFromFile(filename):
    """ simply read all lines from the file and return objects for valid JSON lines """ 
    with open(filename,'rb') as logs:
        for binary_log in logs:
            log_obj = getJsonObjectFromLog(binary_log)
            if log_obj: yield log_obj


""" examples of using the getJsonObjectsFromFile generator """ 

def countJsonProperties(filename):
    properties_count = {}
    for log_obj in getJsonObjectsFromFile(filename):
        for key in log_obj.keys():
            if key in properties_count:
                properties_count[key] += 1
            else:
                properties_count[key] = 1 
    print(properties_count)

def printJsonProperties(filename, properties):
    for log_obj in getJsonObjectsFromFile(filename):
        printstring = ""
        for prop in properties:
            printstring += f'{prop} :: [{log_obj.get(prop)}], '
        print(printstring)


if __name__ == '__main__':
    object_property_to_print = 'message'
    if (len(sys.argv) < 2):
        print("Usage: readJsonFile.py <logfilename> [[str, ...]:object_properties_to_print]")
    else:
        logfileName = sys.argv[1]
        countJsonProperties(logfileName)
    ## if (len(sys.argv) > 2): object_property_to_print = sys.argv[2]
    ## printJsonLogsUsingNext(logfileName, object_property_to_print)
