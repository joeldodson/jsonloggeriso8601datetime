#!/usr/bin/env python3


""" 
I want to be able to read in text, determine if it's JSON 
and print out some of it.

The expectation is each line in the file is syntactically valid JSON.
Lines that are not valid JSON will be ignored.

getJsonObjectsFromFile(filename) will iterate through each line in the file and return an object if the line is valid JSON.
If it is, the specified properties will be printed.
"""


import sys 
import os.path as path 
import typer 
import json 
from typing import List, Dict, Optional, Tuple   


app = typer.Typer()


#######
def getFileComponents(name: str) -> Tuple[str, str, str]:
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

#######
def isJson(tstr: str) -> object:
    """ if tstr is valid JSON, return object created from the string, else, return None """ 
    ret = None
    try:
        ret = json.loads(tstr)
    except ValueError:
        pass
    return ret

#######
def getJsonObjectFromLog(binary_log: str) -> object:
    """ take the binary string and return an object if the string is valid JSON """ 
    log = binary_log.decode(errors='ignore')
    return isJson(log)

#######
def getJsonObjectsFromFile(filename: str) -> object:
    """ simply read all lines from the file and return objects for valid JSON lines """ 
    with open(filename,'rb') as logs:
        for binary_log in logs:
            log_obj = getJsonObjectFromLog(binary_log)
            if log_obj: yield log_obj


""" examples of using the getJsonObjectsFromFile generator """ 

#######
def countJsonProperties(filename: str):
    properties_count = {}
    for log_obj in getJsonObjectsFromFile(filename):
        for key in log_obj.keys():
            if key in properties_count:
                properties_count[key] += 1
            else:
                properties_count[key] = 1 
    typer.echo(json.dumps(properties_count, indent=4))

#######
def printAllProperties(obj: object) -> None:
    typer.echo(obj)

#######
def getPropertyFromObject(obj: object, prop: str, submatch: bool, insensitive: bool) -> object:
    """
    I was using a string to return the property from the object matching the prop parameter
    NOTE: when submatch is True, prop can match more than one property in obj
    now returning a dict of all properties matched 
    """
    ret = {}
    compareKey = ""
    compareProp = prop.lower() if  insensitive else prop  
    for key in obj.keys():
        compareKey = key.lower() if insensitive else key 
        if (submatch and (compareProp in compareKey)) or (compareProp == compareKey):
            """ 
            this conditional does an extra comparison when submatch is true 
            but compareProp is not in compareKey
            it is a nice one-liner though, not counting all these comments 
            maybe I'll change it someday.
            """
            ret[key] = obj[key]
    return ret 

#######
def printMatchObj(obj: object, matchObj: object) -> None: 
    """
    I want to print the matched properties in the same order 
    in which they appear in the original object.
    Since matched properties can be added to matchObj in any order 
    (based on the order of -p on command line, or submatch)
    I use the original object to create the print string.
    """
    printstring = "" 
    for k,v in obj.items():
        if matchObj.get(k, None) != None:
            printstring += f'{k} : {v}, '
    typer.echo(printstring)

#######
def printSpecifiedProperties(obj: object, properties: List[str], submatch: bool, insensitive: bool) -> None:
    """
    print line with each property from obj matching a string in the properties list 
    if no properties in obj are matched by any string in properties list, 
    don't print anything 
    NOTE: with submatch, it's possible for a string in properties to match multiple properties in obj
    or multiple strings in properties could match multiple properties in job.
    keeping track of the matches in a dict addresses this multiple match problem.
    Once all the strings in properties list have been checked, the match dict can be printed as a single line 
    """
    matchObj = {}
    for prop in properties:
        if submatch or insensitive:
            # iterating through each property appears to be the only way to 
            # check if prop is a substring of a property in the object,
            # or to do a case insensitive get() 
            matchObj.update(getPropertyFromObject(obj, prop, submatch, insensitive))
            ## typer.echo(f'current matchObj is {matchObj}')
        else: 
            # if submatch and insensitive are both False, check if the property is in the object
            # if it is, add the property and its value to the match object .
            if obj.get(prop, None) != None:
                matchObj[prop] = obj[prop]
                ## typer.echo(f'current matchObj is {matchObj}')
    if len(matchObj.keys()) > 0:
        printMatchObj(obj, matchObj)

#######
def printJsonProperties(filename: str, properties: Optional[List[str]], all: bool, submatch: bool, insensitive: bool):
    for log_obj in getJsonObjectsFromFile(filename):
        if all:
            printAllProperties(log_obj)
        else: 
            printSpecifiedProperties(log_obj, properties, submatch, insensitive)

#######
# callback makes 'main' the default command to run if no commands are given 
##
## @app.callback(invoke_without_command=True)
# using callback results in help implying there are commands possible after the arguments 
# using app.command shows only the arguments in the help usage first line.
#
@app.command()
def main(jsonfile: str = typer.Argument(...),
        properties: Optional[List[str]] = typer.Option(None, "-p", "--property", help="use multiple -p options to print multiple properties."),   
        all: bool = typer.Option(False, "-a", "--all", help="print all properties, -p options are ignored when this is set"),
        submatch: bool = typer.Option(False, "-s",  "--submatch", help="let specified properties be a substring of a json property, default is whole word match"),
        insensitive: bool = typer.Option(False, "-i",  "--insensitive", help="ignore case when matching property names, default is case sensitive")
) -> None:
    """
    queryjsonfile is kind of like grep focused on properties of JSON objects in a text file.
    if jsonfile is the only argument, a list of the properties, including how often each is present, is printed.
    If a line in the file is not a valid JSON string, it is ignored.
    read the comments after each option to udnerstand how each is used.
    if -a (--all) is present, all -p options are ignored.
    If no -p or -a option is used, -i and -s are ignored.
    """
    typer.echo(f'Querying {jsonfile}')
    if properties or all: 
        printJsonProperties(jsonfile, properties, all, submatch, insensitive)
    else:
        countJsonProperties(jsonfile)

if __name__ == "__main__":
    app()

## end of file 