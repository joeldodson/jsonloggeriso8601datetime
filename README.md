# jsonloggeriso8601datetime Package 

Uses the package 
[python-json-logger](https://pypi.org/project/python-json-logger/) 
as a starting point and adds a simple custom formatter to format the timestamp to comply with ISO8601.  I also add a default config to log to the console and to a log file. 

## Configuration 
I was using a yaml file for configuration.  I wanted to use the same config for gunicorn though and it does not support yaml based config.  So I converted the yaml  config to a dict to use Python's dictConfig.

I've kept the yaml file in the repo for reference.  I added the code that used to be in __init__.py to use the yaml config in the yaml file also for reference. 

the file jsonloggerdictconfig.py, in the package's directory contains default configuration for logging to stdout with minimal information, not JSON formatted.  It also configures a handler to log to a file with much more information and log statements are JSON formatted.

I've created this default configuration with screen readers in mind.  Logging to the console is minimized to avoid a lot of screen reader chatter.  Logging to file is maximized and formatted to support other tools processing those logs and possibly presenting the information in a more accessible way.  Also, if logs are to be processed by any anomaly detection systems, JSON is preferred.

You might notice there's a gunicorn logger in the config file.  I added that to get gunicorn to work with this config.  There might be a better way to do this.  I stopped looking for solutions once I got this working with gunicorn.   
## Dependencies 

See the requirements.txt file for the packages this package requires.

## readjsonfile.py utility 
I wanted to know what the JSON in the log files looked like, e.g., the properties it contained and how consistent each JSON object was.  I also wanted to be able to print only some of the properties (grep/awk would be painful to pick out properties and their values).

readjsonfile.py does this for me.  If you run it with no arguments, a usage line is printed. 
 


