###
# file with some wrappers around other classes 
##

import os 
import logging 
import logging.config
from pythonjsonlogger import jsonlogger 
import datetime


"""
thie idea, and code, to subclass FileHandler came from stackoverflow post:
https://stackoverflow.com/questions/20666764/python-logging-how-to-ensure-logfile-directory-is-created?noredirect=1&lq=1
"""
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
class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """
    extend the JsonFormatter to generate an ISO8601 timestamp 
    """
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['timestamp'] =  datetime.datetime.fromtimestamp(record.created).astimezone().isoformat()


## end of file 