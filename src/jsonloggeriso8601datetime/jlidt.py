""" src/jsonloggeriso8601datetime/jlidt.py 
"""

import logging 
import logging.config

from .jsonloggerdictconfig import defaultJLIDTConfig as defaultConfig

currentConfig = None 

def setConfig(config=defaultConfig):
    global currentConfig
    currentConfig = config
    logging.config.dictConfig(config)


def getCurrentConfig():
    return currentConfig


def getDefaultConfig():
    return defaultConfig


## end of file
