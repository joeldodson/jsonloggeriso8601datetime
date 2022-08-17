#!/usr/bin/env python

import logging 
import jsonloggeriso8601datetime as jlidt 

# jlidt.setConfig() 

if __name__ == '__main__':
    parentLogger = logging.getLogger('parentLogger')
    childLogger = logging.getLogger('parentLogger.childLogger')

    parentLogger.warning("Because I have years of wisdom and want what's best for you.") 
    childLogger.error("you are right, I should listen to you.")

    parentLogger.info('info log from parentLogger')
    childLogger.info('info log from childLogger')

    parentLogger.debug('debug log from parentLogger')
    childLogger.debug('debug log from childLogger')

    parentLogger.warning('warning log from parentLogger')
    childLogger.warning('warning log from childLogger')

    parentLogger.info('test to add extra parameters', extra={ 'parm1':1, 'parm2':4})


