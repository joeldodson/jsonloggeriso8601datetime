# jsonloggeriso8601datetime Package

This package is mainly about providing an out of the box configuration to enable the builtin Python logging package to generate logs as JSON.  
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
As noted above, you can see the values of the default configuration by running ``` python -m jsonloggeriso8601datetime -d  ```.
I've created this default configuration with screen readers in mind.
Logging to the console is minimized to avoid a lot of screen reader chatter.
Logging to a file is maximized and formatted to support other tools processing those logs and possibly presenting the information in a more accessible way.
Also, if logs are to be processed by any anomaly detection systems, JSON is probably best.

The log level for both console and JSON file defaults to "INFO".
that can be changed by setting environment variables to the desired level.
For example, in PowerShell:
``` sh
Env:JLIDT_CONSOLE_LEVEL = "DEBUG"
Env:JLIDT_JSONFILE_LEVEL = "WARNING"
```
will set the console logger to DEBUG and the JSON file logger to WARNING.

You might notice there's a gunicorn logger in the config file.
I added that to get gunicorn to work with this default config.
There might be a better way to do this.  I stopped looking for solutions once I got this working with gunicorn.

## Dependencies

The python-json-logger is the only requirement at time of writing.
It's unfortunately going through some possible abandonment issues.
A new maintainer (nhairs) has stepped up and made many fixes.
Unfortunately the current maintainer does not aappear to be responding and merging PRs.
Thus, [python-json-logger is currently being pulled from github](https://github.com/nhairs/python-json-logger).
That repo page has information regarding the process of switching maintainers.

### temporary workaround 

Turns out PyPI does not like people uploading packages with dependencies pointing to github.
To be able to publish this package, I copied pythonjsonlogger source code to 
the src directory in jsonloggeriso8601datetime as jlidt_pjl.
This is a temporary solution and 
I added a README  file in that directory to explain it.
Once ownership of python-json-logger is resolved,
I will delete my local copy of pythonjsonlogger source code.

## Scripts

Some simple functionality is provided directly from `jsonloggeriso8601datetime` itself using `python -m`. Run:

``` sh
python -m jsonloggeriso8601datetime --help
```

to see what is available.
As of v1.0.4, you can pretty print the default config to stdout.
You can also run a simple example to check the default config, to determine if it's sufficient.
As noted above, it's currently set to INFO for both the  console and file loggers and changeable using environment variables.

### jilqs (Json Iso8601 Logger Query Script)

jilqs is installed as a script by default (not as an extra).
I decided to do this for simplicity, 
and the name is bad enough it's unlikely to conflict with anything else on your system.
It's very light weight and uses only standard Python.
Run:

``` sh
 jilqs --help 
```

to see what it does.

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

## Wrapping It Up

If you like this functionality and want to extend it, I suggest starting with python-json-logger.
The documentation there is very good and it seems to be a popular package on PyPI.
You're even welcome to take my extension and add it to whatever you do to extend python-json-logger.

I built this package really for my own opinions and added it to PyPI so I could pip install it instead of copying it around to different projects.
Also I can import it to the REPL and easily get logs in a file.

If others like this default config and ISO8601 timestamps, great.
Enjoy the package and feel free to open issues on github.

Cheers!!
