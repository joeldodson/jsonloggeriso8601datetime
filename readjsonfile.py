#!/usr/bin/env python3
""" 
I want to be able to read in text, determine if it's JSON 
and print out some of it.

generator that returns objects from files containing lines of text each which is syntactically valid JSON

lazy iterator to get JSON objects from file.
The expectation is each line in the file is syntactically valid JSON.
Lines that are not valid JSON will be ignored.

getJsonObjectsFromFile(filename) will iterate through each line in the file and return an object if the line is valid JSON
"""


import sys 
import os.path as path 
import typer 
import json 
from typing import List 
from typing import Dict 


app = typer.Typer()


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
    print(json.dumps(properties_count, indent=4))


def printJsonProperties(filename, properties):
    for log_obj in getJsonObjectsFromFile(filename):
        printstring = ""
        for prop in properties:
            printstring += f'{prop} = {log_obj.get(prop)}, '
        print(printstring)


if __name__ == '__main__':
    properties = ['message']
    if len(sys.argv) < 2:
        print("Usage: readJsonFile.py <jsonfilename> [str [, str, ...]:object_properties_to_print]")
    else:
        logfileName = sys.argv[1]
        if len(sys.argv) == 2: 
            countJsonProperties(logfileName)
        else:
            properties = sys.argv[2:]
            print(f'properties is {properties}')
            printJsonProperties(logfileName, properties)

 
#######
# callback makes 'main' the default command to run if no commands are given 
##
@app.callback(invoke_without_command=True)
def main(jsonFilename: str,
        property: str = typer.Option(None, "--property", "-p"),
        caseSensitive: bool = typer.Option(False, "--caseSensitive", "-c"),
) -> None:
    if property: 
            shortcuts = filterShortcuts(searchStr)
        printShortcuts(pageSize, when)


if __name__ == "__main__":
    app()
    ## typer.run(main)

## end of file 