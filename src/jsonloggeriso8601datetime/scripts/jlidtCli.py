""" src/jsonloggeriso8601datetime/jlidtCli.py """

import logging 
import json 

import jsonloggeriso8601datetime as jlidt 
jlidt.setConfig() ## uses the default config from the jsonloggeriso8601datetime package 

## Define the command line interface
import argparse

jlidtCli_description = """ Run simple commands from the jsonloggeriso8601datetime module """

example_help = """ some example logging using the default config."""

print_default_config_help = """ prints the default config to stdout.
You can redirect to a config.py file to customize the config.
"""


parser = argparse.ArgumentParser(
    prog="jlidtCli",
    description=jlidtCli_description,
    formatter_class=argparse.RawTextHelpFormatter,
    epilog="Cheers!",
)
parser.add_argument("-e", "--example", action="store_true", help=example_help)
parser.add_argument(
    "-d", "--defaultconfig", action="store_true", help=print_default_config_help
)
args = parser.parse_args()


def printDefaultConfig():
    print(json.dumps(jlidt.getDefaultConfig(), indent=4))


def example():
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
        return example()
    if args.defaultconfig:
        print("Default configuration from jsonloggeriso8601datetime is:")
        return printDefaultConfig()
    print("try running with --help")

if __name__ == "__main__":
    run()


## end of file 