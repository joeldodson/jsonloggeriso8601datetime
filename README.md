# jsonloggeriso8601datetime Package

This package is mainly about providing an out of the box configuration to enable the built-in Python logging package to generate logs as JSON.  
It starts with the package
[python-json-logger](https://pypi.org/project/python-json-logger/) 
and adds a simple custom formatter to format the timestamp to comply with ISO8601 formats.
It also provides a default config to log to the console and to a log file. 
After installing the package, run
``` sh
python -m jsonloggeriso8601datetime --example
```
to see the default console logging output.
And look in ``` logs/jsonLogs.log ``` to see the default file logging output.

If you're happy with the default configuration, the basic use case is all you need.
If you want to change the configuration (e.g., add more properties to the file output, change default logging levels), pass in a modified dict to setConfig().
You can get the default config using:

``` sh 
python -m jsonloggeriso8601datetime -d > myCustomConfig.py
```

edit myConfig.py to give the dict a variable name, then import myConfig, name you gave your dict variable, to your project and use that dict in setConfig. 

For the log file output, the package will ensure the directory exists before trying to write to the log file.
This is done by the MakedirFileHandler class
(in src/jsonloggeriso8601datetime/wrappers.py).

## Scripts

After you ``` pip install jsonloggeriso8601datetime ```, or however you manage your python environment,
you will have two new scripts available from the command line.

### jlidtCli

``` jlidtCli ``` is for json logger iso8601 datetime Command line interface.
You can use this script instead of the longer example above of invoking the module using the ```-m``` option.
Run,

``` bash 
jlidtCli --help
```

for how it works.

### jlidtQs

``` jlidtQs ``` is the same as above with Query String added.
It is a program to parse and analyze the JSON formatted log files.
It was named ```jilqs```, changed it for consistency.
Run, 

``` bash 
jlidtQs --help
```

for details.

## How To Use jsonloggeriso8601datetime

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
As noted above, you can see the values of the default configuration by running ``` python -m jsonloggeriso8601datetime -d  ```,
(or, the easier ``` jlidtCli -d ``` as noted in the scripts section ).
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

The log files will, by default, be written to ```./logs/jsonLogs.log```.
There is an environment variable to change this too.  Try,

``` sh
$Env:JLIDT_JSONFILE_PATHNAME = "my/path/my-filename.log"
```

You might notice there's a gunicorn logger in the config file.
I added that to get gunicorn to work with this default config.
There might be a better way to do this.  I stopped looking for solutions once I got this working with gunicorn.

## Dependencies

The python-json-logger is the only requirement at time of writing.
See notes in the changes for 2.0.0 regarding this package.

## Version History

### 1.0.1

* initial package plus typo fix

### 1.0.2

* moved the repo from github.om/blindgumption to github.com/joeldodson
* changed default log levels to INFO and provided env vars option to set different levels

### 1.0.3

* typo in pyproject and using pip-tools changed requirements.txt 

### 1.0.4

- Significant changes but basic usage for logging is backward compatible
- moved project to poetry 
  (I've been using poetry on other projects and didn't want to go back and remember how to release using hatch).
- moved functionality supported by jlidtexample and jlidtdefaultconfig
  into the module itself.
  See notes above under the Scripts heading.
- introduced jilqs (see note above under Scripts heading)

### 1.0.5

- copied python-json-logger source code into jsonloggeriso8601datetime repo.
  This has been noted in the main README and a README created in the jlidt_pjl source directory.
  I decided to bump the version for this to keep it separate from anything else.

### 2.0.0 

- major version bump:  the logging itself is backward compatible, but I changed the name of jilqs to be consistent.
- added script, ```jlidt``` for simplicity, don't have to run with ```python -m```
- upgraded to poetry 2.x
- python-json-logger ownership has been resolved.  Back to the pypi version now
- restructured code to be a bit more pythonic

### 3.0.0 - 2025-04-30 

- big changes to repo structure.
- the major version of 3 is more about me dithering around with poetry 2 and pyproject.toml 
  than the maturity of the project.
  Though the project is pretty mature and I don't expect many more big changes.
- changed script ``` jlidt ``` to ``` jlidtCli ```   
- got rid of extra package for the scripts.
  Added a scripts sub directory in the main jsonloggeriso8601datetime and moved jlidtCli and jlidtQs there,
  and updated pyproject.toml to install both with the jsonloggeriso8601datetime project.

## Wrapping It Up

If you like this functionality and want to extend it, I suggest starting with python-json-logger.
The documentation there is very good and it seems to be a popular package on PyPI.
You're even welcome to take my extension and add it to whatever you do to extend python-json-logger.

I built this package really for my own opinions and added it to PyPI so I could pip install it instead of copying it around to different projects.
Also I can import it to the REPL and easily get logs in a file.

If others like this default config and ISO8601 timestamps, great.
Enjoy the package and feel free to open issues on github.

Cheers!!
