"""  jsonloggeriso8601datetime/__init__.py 
wrapper on logging to use JSON for log to file output 

Sssee https://pypi.org/project/python-json-logger/  for JSON formatting 
logs to stdout will be as simple as possible to avoid long gibberish from the screen reader.
Could not get the python logging module to format the timestamp in the iso8601 format I wanted.
was able to find way using datetime and CustomJasonFormatter 
"""

import logging 
import logging.config
import json

from .wrappers import MakedirFileHandler 
from .wrappers import CustomJsonFormatter 
from .jsonloggerdictconfig import defaultJLIDTConfig  as defaultConfig 

currentConfig = None

#######
def setConfig(config = defaultConfig):
    global currentConfig 
    currentConfig = config 
    logging.config.dictConfig(config)

#######
def getCurrentConfig():
    return currentConfig 

#######
def getDefaultConfig():
    return defaultConfig 


###
def printDefaultConfig():
    print(json.dumps(defaultConfig, indent=4)) 

###
def printCurrentConfig():
    print(json.dumps(currentConfig, indent=4))


#######
def example():
    setConfig()
    parentLogger = logging.getLogger('parentLogger')
    childLogger = logging.getLogger('parentLogger.childLogger')
    parentLogger.warning("Because I have years of wisdom and want what's best for you.") 
    childLogger.error("you are right, I should listen to you.")
    parentLogger.info('info log from parentLogger')
    childLogger.info('info log from childLogger')
    parentLogger.debug('debug log from parentLogger')
    childLogger.debug('debug log from childLogger')
    parentLogger.warning('warning log from parentLogger')
    childLogger.warning('warning log from childLogger')
    parentLogger.info('test to add extra parameters', extra={ 'parm1':1, 'parm2':4})


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.warn("do not seek the treasure")


## end of file
