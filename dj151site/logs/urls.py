
from django.conf.urls import patterns, include, url

urlpatterns = patterns('logs.views',
                       # url(r'^$', 'dj14site.views.home', name='home'),
                       # url(r'^dj14site/', include('dj14site.foo.urls')),
                       #my_url
                       url(r'^$', 'welcome'),
                       url(r'^welcome$', 'welcome'),
                       url(r'^index/$', 'index'),
                       )
