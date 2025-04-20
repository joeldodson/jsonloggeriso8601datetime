""" src/jsonloggeriso8601datetime/main.py 
thie idea, and code, to subclass FileHandler came from stackoverflow post:
https://stackoverflow.com/questions/20666764/python-logging-how-to-ensure-logfile-directory-is-created?noredirect=1&lq=1
"""

import os 
import logging 
import logging.config
import datetime
import json 

## from jlidt_pjl import jsonlogger
from pythonjsonlogger.json import JsonFormatter

from .jsonloggerdictconfig import defaultJLIDTConfig as defaultConfig

## Define the command line interface
import argparse

jlidt_description = (
    """ Run simple commands from the jsonloggeriso8601datetime module """
)

example_help = """ some example logging using the default config."""

print_default_config_help = """ prints the default config to stdout.
You can redirect to a config.py file to customize the config.
"""

print_current_config_help = """ prints the current config to stdout.
Maybe you want to check your config settings?
"""

parser = argparse.ArgumentParser(
    prog="jlidt",
    description=jlidt_description,
    formatter_class=argparse.RawTextHelpFormatter,
    epilog="Cheers!",
)
parser.add_argument("-e", "--example", action="store_true", help=example_help)
parser.add_argument(
    "-d", "--defaultconfig", action="store_true", help=print_default_config_help
)
parser.add_argument(
    "-c", "--currentconfig", action="store_true", help=print_current_config_help
)
args = parser.parse_args()


#######
def mkdir_p(path):
    """http://stackoverflow.com/a/600612/190597 (tzot)"""
    try:
        os.makedirs(path, exist_ok=True)  # Python>3.2
    except TypeError as ex:
        print(f'TypeError while trying to create directory {path}, error: {ex}')

#######
class MakedirFileHandler(logging.FileHandler):
    def __init__(self, filename, mode='a', encoding=None, delay=0):            
        mkdir_p(os.path.dirname(filename))
        super(MakedirFileHandler, self).__init__(filename, mode, encoding, delay)

#######
class CustomJsonFormatter(JsonFormatter):
    """
    extend the JsonFormatter to generate an ISO8601 timestamp 
    """
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['timestamp'] =  datetime.datetime.fromtimestamp(record.created).astimezone().isoformat()


currentConfig = None 
#######
def setConfig(config=defaultConfig):
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
    parentLogger = logging.getLogger("parentLogger")
    childLogger = logging.getLogger("parentLogger.childLogger")
    parentLogger.warning("Because I have years of wisdom and want what's best for you.")
    childLogger.error("you are right, I should listen to you.")
    parentLogger.info("info log from parentLogger")
    childLogger.info("info log from childLogger")
    parentLogger.debug("debug log from parentLogger")
    childLogger.debug("debug log from childLogger")
    parentLogger.warning("warning log from parentLogger")
    childLogger.warning("warning log from childLogger")
    parentLogger.info("test to add extra parameters", extra={"parm1": 1, "parm2": 4})


def run():
    if args.example:
        example()
    if args.defaultconfig:
        print("Default configuration from jsonloggeriso8601datetime is:")
        printDefaultConfig()
    if args.currentconfig:
        print("Current configuration from jsonloggeriso8601datetime is:")
        printCurrentConfig()


if __name__ == "__main__":
    run()


## end of file
