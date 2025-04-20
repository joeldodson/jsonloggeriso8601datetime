"""src/jsonloggeriso8601datetime/jsonloggerdictconfig.py 
default Json Logger Iso8601 Date Time Config
"""

import os

defaultJLIDTConfig = {
    "version": 1,
    ## "incremental": False,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "format": "%(levelname)s -- %(message)s -- %(module)s:%(lineno)d, %(name)s"
        },
        "jsonFile": {
            # see https://docs.python.org/3/library/logging.config.html to understand the "()" key
            "()": "jsonloggeriso8601datetime.CustomJsonFormatter",
            "format": "%(timestamp)s %(module)s %(lineno)d %(name)s %(levelname)s %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            ## "level": "DEBUG",
            "level": os.getenv("JLIDT_CONSOLE_LEVEL", "INFO"),
            "formatter": "console",
            "stream": "ext://sys.stdout",
        },
        "jsonFile": {
            ## "class": "logging.FileHandler",
            "()": "jsonloggeriso8601datetime.MakedirFileHandler",
            ## "level": "DEBUG",
            "level": os.getenv("JLIDT_JSONFILE_LEVEL", "INFO"),
            "formatter": "jsonFile",
            "filename": os.getenv("JLIDT_JSONFILE_PATHNAME","./logs/jsonLogs.log"),
            "encoding": "utf8",
        },
    },
    "loggers": {
        "gunicorn": {
            "level": "INFO",
            "propagate": False,
            "handlers": ["console", "jsonFile"],
        },
    },
    "root": {"level": "DEBUG", "handlers": ["console", "jsonFile"]},
}

## end of file
