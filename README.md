# MX Logging

A logging UI for python project

## Simple Example

```python
import logging
from mxlogging import MXLoggingHandler, MXLoggingUI

logger = logging.getLogger('simple_example')

handler = MXLoggingHandler()
logger.addHandler(handler)

# Launch GUI 
MXLoggingUI.launch() 

# Start logging
logger.debug("MX Logging Example")

```
