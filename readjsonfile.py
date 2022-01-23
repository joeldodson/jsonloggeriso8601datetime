###
# # #!/usr/bin/env python3


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
from typing import List, Dict, Optional  


app = typer.Typer()


#######
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

#######
def isJson(tstr):
    """ if tstr is valid JSON, return object created from the string, else, return None """ 
    ret = None
    try:
        ret = json.loads(tstr)
    except ValueError:
        pass
    return ret

#######
def getJsonObjectFromLog(binary_log):
    """ take the binary string and return an object if the string is valid JSON """ 
    log = binary_log.decode(errors='ignore')
    return isJson(log)

#######
def getJsonObjectsFromFile(filename):
    """ simply read all lines from the file and return objects for valid JSON lines """ 
    with open(filename,'rb') as logs:
        for binary_log in logs:
            log_obj = getJsonObjectFromLog(binary_log)
            if log_obj: yield log_obj


""" examples of using the getJsonObjectsFromFile generator """ 

#######
def countJsonProperties(filename):
    properties_count = {}
    for log_obj in getJsonObjectsFromFile(filename):
        for key in log_obj.keys():
            if key in properties_count:
                properties_count[key] += 1
            else:
                properties_count[key] = 1 
    typer.echo(json.dumps(properties_count, indent=4))


#######
def printJsonProperties(filename, properties, all, insensitive):
    for log_obj in getJsonObjectsFromFile(filename):
        if all:
            typer.echo(log_obj)
        else:
            printstring = ""
            for prop in properties:
                printstring += f'{prop} = {log_obj.get(prop)}, '
            typer.echo(printstring)


#######
# callback makes 'main' the default command to run if no commands are given 
##
@app.callback(invoke_without_command=True)
def main(jsonFilename: str = typer.Argument(...),
        properties: Optional[List[str]] = typer.Option(None, "-p", "--property", help="use multiple -p options to print multiple properties."),   
        all: bool = typer.Option(False, "-a", "--all", help="print all properties, -p flags are ignored when this is set"),
        insensitive: bool = typer.Option(False, "-i",  "--insensitive", help="ignore case when matching property names, default is case sensitive")
) -> None:
    if properties or all: 
        printJsonProperties(jsonFilename, properties, all, insensitive)
    else:
        countJsonProperties(jsonFilename)

if __name__ == "__main__":
    app()
    ## typer.run(main)

## end of file 