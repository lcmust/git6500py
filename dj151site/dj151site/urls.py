from django.conf.urls import patterns, include, url
import os
DIR_HERE = os.path.dirname(__file__)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'dj151site.views.home', name='home'),
                       # url(r'^dj151site/', include('dj151site.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       # static_blog:css js img
                       #url(r'^static_blog/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'/home/love/git6500py/dj151site/dj151site/static/'}),
                       url(r'^static_blog/css/(?P<path>.*)$', 'django.views.static.serve', {'document_root':os.path.dirname(DIR_HERE) + "/static/css/"}),
                       url(r'^static_blog/js/(?P<path>.*)$', 'django.views.static.serve', {'document_root':os.path.dirname(DIR_HERE) + "/static/js/"}),
                       url(r'^static_blog/img/(?P<path>.*)$', 'django.views.static.serve', {'document_root':os.path.dirname(DIR_HERE) + "/static/img/"}),

                       url(r'^blog/', include('blog.urls')),
                       url(r'^logs/', include('logs.urls')),
                       url(r'^polls/', include('polls.urls', namespace="polls")),
                       #url(r'^blog/', 'blog.views.home'),
                       #url(r'^author/', include('blog.urls')),
                       )
