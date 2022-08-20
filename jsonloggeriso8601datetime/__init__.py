"""  jsonloggeriso8601datetime/__init__.py 
wrapper on logging to use JSON for log to file output 

Sssee https://pypi.org/project/python-json-logger/  for JSON formatting 
logs to stdout will be as simple as possible to avoid long gibberish from the screen reader.
Could not get the python logging module to format the timestamp in the iso8601 format I wanted.
was able to find way using datetime and CustomJasonFormatter 
"""

import os 
import logging 
import logging.config
from pythonjsonlogger import jsonlogger 
import datetime
from .wrappers import MakedirFileHandler 
from .wrappers import CustomJsonFormatter 
from .jsonloggerdictconfig import defaultJLIDTConfig  as defaultConfig 

currentLoggingConfig = None

#######
def setConfig(config = defaultConfig):
    global currentLoggingConfig 
    currentLoggingConfig = config 
    logging.config.dictConfig(config)

####### 
def getCurrentConfig():
    return currentLoggingConfig 

####### 
def getDefaultConfig():
    return defaultConfig 


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.warn("do not seek the treasure")


## end of file 