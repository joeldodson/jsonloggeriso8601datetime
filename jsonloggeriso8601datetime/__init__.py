
"""
wrapper on logging to use JSON for log to file output 

Sssee https://pypi.org/project/python-json-logger/  for JSON formatting 
logs to stdout will be as simple as possible to avoid long gibberish from the screen reader.
Could not get the python logging module to format the timestamp in the iso8601 format I wanted.
was able to find way using datetime and CustomJasonFormatter 

Configuration WAS in jsonloggerconfig.yaml 
switched to dict config (jsonloggerdictconfig.py) to use same file with gunicorn configuration 
"""

import logging 
import logging.config
from pythonjsonlogger import jsonlogger 
import datetime


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """
    extend the JsonFormatter to generate an ISO8601 timestamp 
    """
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['timestamp'] =  datetime.datetime.fromtimestamp(record.created).astimezone().isoformat()


from .jsonloggerdictconfig import dictConfig 
logging.config.dictConfig(dictConfig)

def getJsonLogger(name):
    return logging.getLogger(name) 


if __name__ == '__main__':
    print("you really ought to run the testjsonlogger.py file in the project's root directory")


