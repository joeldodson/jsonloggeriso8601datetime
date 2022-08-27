# jsonloggeriso8601datetime Package

This package is mainly about providing an out of the box configuration to enable the builtin Python logging package to generate logs as JSON.  
It starts with the package
[python-json-logger](https://pypi.org/project/python-json-logger/) 
and adds a simple custom formatter to format the timestamp to comply with ISO8601 formats.
It also provides a default config to log to the console and to a log file. 
After installing the package, run
``` sh
$ jlidtexample 
```
to see the default console logging output.
look in ``` logs/jsonLogs.log ``` to see the default file logging output.

If you're happy with the default configuration, the basic use case is all you need.
If you want to change the configuration (e.g., add more properties to the file output, change default logging levels), pass in a modified dict to setConfig().
You can start with the default config using the script jlidtdefaultconfig, redirect to a file, then edit that file accordingly.
For example:
``` sh
$ jlidtdefaultconfig > myCustomConfig.py
```
edit myConfig.py to give the dict a variable name, then import myConfig, name you gave your dict variable, to your project and use that dict in setConfig. 

For the log file output, the package will ensure the directory exists before trying to write to the log file.
This is done by the MakedirFileHandler class.
Check out the wrappers.py module in jsonloggeriso8601datetime package if you're curious.

## How To Use

Add the below lines to the beginning of the main python file (where __name__ == "__main__"):

``` python
import logging
import jsongloggeriso8601datetime as jlidt
jlidt.setConfig()  # using the provided default configuration 
```

This will configure a root logger which, from my understanding of Python logging, will result in all subsequent logs to use that configuration (unless specifically overridden).

## Configuration

The file jsonloggerdictconfig.py, in the package's directory contains default configuration for logging to stdout with minimal information, not JSON formatted.
It also configures a handler to log to a file with much more information and log statements are JSON formatted.
As noted above, you can see the values of the default configuration by running ``` jlidtdefaultconfig ```.
I've created this default configuration with screen readers in mind.
Logging to the console is minimized to avoid a lot of screen reader chatter.
Logging to a file is maximized and formatted to support other tools processing those logs and possibly presenting the information in a more accessible way.
Also, if logs are to be processed by any anomaly detection systems, JSON is probably best.

The log level for both console and JSON file defaults to "INFO".
that can be changed by setting environment variables to the desired level.
For example, in PowerShell:
``` sh
$Env:JLIDT_CONSOLE_LEVEL = "DEBUG"
$Env:JLIDT_JSONFILE_LEVEL = "WARNING"
```
will set the console logger to DEBUG and the JSON file logger to WARNING.

You might notice there's a gunicorn logger in the config file.
I added that to get gunicorn to work with this default config.
There might be a better way to do this.  I stopped looking for solutions once I got this working with gunicorn.

## Dependencies

See the requirements.txt file for the details of packages this package requires.
Short answer though is python-json-logger 2.0.4 is the only requirement at time of writing.

## Scripts

Two very small scripts (entry points) are shipped with this package.
``` sh
jlidtdefaultconfig
```
and 
``` sh 
jlidtexample
```
should both be installed as part of the pip installation.

jlidtDefaultConfig has already been described.  jlidtExample.py uses jsonloggeriso8601datetime with its default config.
You can run that to determine if the default config is sufficient.
As noted above, it's currently set to INFO for both the  console and file loggers and changeable using environment variables.

## Version History

### 1.0.1

initial package plus typo fix

### 1.0.2

* moved the repo from github.om/blindgumption to github.com/joeldodson
* changed default log levels to INFO and provided env vars option to set different levels

## Wrapping It Up

If you like this functionality and want to extend it, I suggest starting with python-json-logger.
The documentation there is very good and it seems to be a popular package on PyPI.
You're even welcome to take my extension and add it to whatever you do to extend python-json-logger.

I built this package really for my own opinions and added it to PyPI so I could pip install it instead of copying it around to different projects.
Also I can import it to the REPL and easily get logs in a file.

If others like this default config and ISO8601 timestamps, great.
Enjoy the package and feel free to open issues on github.

Cheers!!
