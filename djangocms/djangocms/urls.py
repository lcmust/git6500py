from django.conf.urls.defaults import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = i18n_patterns('', 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
    )

if settings.DEBUG:
    urlpatterns = patterns('', 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns

###
###urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangocms.views.home', name='home'),
    # url(r'^djangocms/', include('djangocms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
###)
