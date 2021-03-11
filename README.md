# jsonloggeriso8601datetime Package 
simple wrapper around a JSON custom formatter.  Added another layer of custom formatter to get ISO 8601 date/time format for log timestamps.

## Configuration 
the file jsonloggerconfig.yaml, in the package's directory contains default configuration for logging to stdout with minimal information, not JSON formatted.  It also configures a handler to log to a file with much more information and log statements are JSON formatted.

I've created this default configuration with screen readers in mind.  Logging to the console is minimized to avoid a lot of screen reader chatter.  Logging to file is maximized and formatted to support other tools processing those logs and possibly presenting the information in a more accessible way.  Also, if logs are to be processed by any anomaly detection systems, JSON is preferred.

## Dependencies 

See the requirements.txt file for the JSON logger and YAML (and maybe others at some point) packages this package requires. 


