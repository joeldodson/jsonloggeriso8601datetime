""" jsonloggeriso8601datetime/src/jsonloggeriso8601datetime/__main__.py 

use the -m flag to run simple items from the jsonloggeriso8601datetime module
"""

import logging
import jsonloggeriso8601datetime as jlidt
jlidt.setConfig()


## Define the command line interface
import argparse

jlidt_description = (
    """ Run simple commands from the jsonloggeriso8601datetime module """
)

example_help = """ some example logging using the default config."""

print_default_config_help = """ prints the default config to stdout.
You can redirect to a config.py file to customize the config.
"""

print_current_config_help = """ prints the current config to stdout.
Maybe you want to check your config settings?
"""

parser = argparse.ArgumentParser(
    prog="jsonloggeriso8601datetime",
    description=jlidt_description,
    formatter_class=argparse.RawTextHelpFormatter,
    epilog="Cheers!",
)
parser.add_argument("-e", "--example", action="store_true", help=example_help)
parser.add_argument(
    "-d", "--defaultconfig", action="store_true", help=print_default_config_help
)
parser.add_argument(
    "-c", "--currentconfig", action="store_true", help=print_current_config_help
)
args = parser.parse_args()


def main():
    if args.example:
        jlidt.example()
    if args.defaultconfig:
        print("Default configuration from jsonloggeriso8601datetime is:")
        jlidt.printDefaultConfig()
    if args.currentconfig:
        print("Current configuration from jsonloggeriso8601datetime is:")
        jlidt.printCurrentConfig()


if __name__ == "__main__":
    main()


## end of file
