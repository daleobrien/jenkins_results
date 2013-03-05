from django.conf.urls import patterns, url
from views import result


urlpatterns = patterns('',

    url(r'^job/(?P<project>\w+)/$', result)
)
