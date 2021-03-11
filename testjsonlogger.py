#!/usr/bin/env python3

from jsonloggeriso8601datetime import getJsonLogger


if __name__ == '__main__':
    parentLogger = getJsonLogger('parentLogger')
    childLogger = getJsonLogger('parentLogger.childLogger')

    parentLogger.info('info log from parentLogger')
    childLogger.info('info log from childLogger')

    parentLogger.debug('debug log from parentLogger')
    childLogger.debug('debug log from childLogger')

    parentLogger.warning('warning log from parentLogger')
    childLogger.warning('warning log from childLogger')

    parentLogger.info('test to add extra parameters', extra={ 'parm1':1, 'parm2':4})


