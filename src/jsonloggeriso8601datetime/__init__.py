"""  src/jsonloggeriso8601datetime/__init__.py 
wrapper around logging to use JSON for log to file output 

Sssee https://pypi.org/project/python-json-logger/  for JSON formatting 
logs to stdout will be as simple as possible to avoid long gibberish from the screen reader.
Could not get the python logging module to format the timestamp in the iso8601 format I wanted.
was able to find way using datetime and CustomJasonFormatter 
"""

from .jlidt import (
    setConfig,
    getCurrentConfig,
    getDefaultConfig,
)

from jsonloggeriso8601datetime.wrappers import CustomJsonFormatter, MakedirFileHandler
## import wrappers


if __name__ == '__main__':
    print("do not execute this module")


## end of file
