
"""
wrapper on logging to use JSON for log to file output 

Sssee https://pypi.org/project/python-json-logger/  for JSON formatting 
logs to stdout will be as simple as possible to avoid long gibberish from the screen reader.
Could not get the python logging module to format the timestamp in the iso8601 format I wanted.
was able to find way using datetime and CustomJasonFormatter 

Configuration is in jsonloggerconfig.yaml 
"""

import logging 
import logging.config
from pythonjsonlogger import jsonlogger 
import datetime
import yaml



class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """
    extend the JsonFormatter to generate an ISO8601 timestamp 
    """
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['timestamp'] =  datetime.datetime.fromtimestamp(record.created).astimezone().isoformat()


"""
read in the yaml based logging configuration 
If you make any config changes, I suggest you run ../testjsonlogger.py 
to ensure your changes didn't break anything.
As you can see, there is no exception/error handling when reading in the config.
It's up to the user to test their config changes before using this logging wrapper.
"""
with open('./jsonloggeriso8601datetime/jsonloggerconfig.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)


def getJsonLogger(name):
    return logging.getLogger(name) 


if __name__ == '__main__':
    print("you really ought to run the testjsonlogger.py file in the package's root directory")


