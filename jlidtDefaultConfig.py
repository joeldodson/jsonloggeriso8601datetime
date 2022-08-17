#!/usr/bin/env python
""" 
use this to get a print out of the default configuration for jsonloggeriso8601datetime 
"""

import json 
import jsonloggeriso8601datetime as jlidt 

config = jlidt.getDefaultConfig()
print(json.dumps(config, indent=4)) 

## end of file 