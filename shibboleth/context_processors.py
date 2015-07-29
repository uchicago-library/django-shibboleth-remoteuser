import sys
from django.core.urlresolvers import reverse
if (sys.version_info < (3, 0)):
    from urllib import quote
else:
    from urllib.parse import quote

def login_link(request):
    """
    This assumes your login link is the Shibboleth login page for your server 
    and uses the 'target' url parameter.
    """
    full_path = quote(request.get_full_path())
    login = reverse('shibboleth:login')
    ll = "%s?target=%s" % (login, full_path)
    return { 'login_link': ll }

def logout_link(request, *args):
    """
    This assumes your login link is the Shibboleth login page for your server 
    and uses the 'target' url parameter.
    e.g: https://school.edu/Shibboleth.sso/Login
    """
    if (sys.version_info < (3, 0)):
        from app_settings import LOGOUT_URL, LOGOUT_REDIRECT_URL
    else:
        from .app_settings import LOGOUT_URL, LOGOUT_REDIRECT_URL
    #LOGOUT_REDIRECT_URL specifies a default logout page that will always be used when
    #users logout from Shibboleth.
    target = LOGOUT_REDIRECT_URL or quote(request.build_absolute_uri())
    logout = reverse('shibboleth:logout')
    ll = "%s?target=%s" % (logout, target)
    return { 'logout_link': ll }
