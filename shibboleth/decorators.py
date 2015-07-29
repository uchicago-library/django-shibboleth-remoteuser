"""
Decorators to use with Shibboleth.
"""
import sys
from django.conf import settings
from django.contrib import auth
if (sys.version_info < (3, 0)):
    from middleware import ShibbolethRemoteUserMiddleware
else:
    from .middleware import ShibbolethRemoteUserMiddleware

def login_optional(func):
  """
  Decorator to pull Shib attributes and log user in, if possible.  Does not 
  enforce login.
  """
  def decorator(request,*args, **kwargs):
    #Do nothing if the remoteuser backend isn't activated
    if 'shibboleth.backends.ShibbolethRemoteUserBackend' not in settings.AUTHENTICATION_BACKENDS:
        pass
    else:
        shib = ShibbolethRemoteUserMiddleware()
        #Proccess the request with the Shib middlemare, which will log the
        #user in if we can.
        proc = shib.process_request(request)
    return func(request, *args, **kwargs)
  return decorator 
