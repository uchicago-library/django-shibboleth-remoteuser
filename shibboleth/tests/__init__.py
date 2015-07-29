import sys
if (sys.version_info < (3, 0)):
    from shib import *
else:
    from .shib import *
