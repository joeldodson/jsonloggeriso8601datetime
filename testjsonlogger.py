#!/usr/bin/env python3

import logging 
import jsonloggeriso8601datetime as jlidt 

jlidt.setConfig() 

if __name__ == '__main__':
    parentLogger = logging.getLogger('parentLogger')
    childLogger = logging.getLogger('parentLogger.childLogger')

    parentLogger.warning("using dict config now") 
    childLogger.warning("okay boomer, go back to your dict config, yaml is too hip for you.")

    parentLogger.info('info log from parentLogger')
    childLogger.info('info log from childLogger')

    parentLogger.debug('debug log from parentLogger')
    childLogger.debug('debug log from childLogger')

    parentLogger.warning('warning log from parentLogger')
    childLogger.warning('warning log from childLogger')

    parentLogger.info('test to add extra parameters', extra={ 'parm1':1, 'parm2':4})


