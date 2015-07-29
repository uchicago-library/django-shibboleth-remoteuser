import sys
from distutils.version import StrictVersion
import django
if StrictVersion(django.get_version()) < StrictVersion('1.4'):
    from django.conf.urls.defaults import *
else:
    from django.conf.urls import patterns, url

if (sys.version_info < (3, 0)):
    from views import ShibbolethView, ShibbolethLogoutView, ShibbolethLoginView
else:
    from .views import ShibbolethView, ShibbolethLogoutView, ShibbolethLoginView

urlpatterns = patterns('',
    url(r'^login/$', ShibbolethLoginView.as_view(), name='login'),
    url(r'^logout/$', ShibbolethLogoutView.as_view(), name='logout'),
    url(r'^$', ShibbolethView.as_view(), name='info'),
)
