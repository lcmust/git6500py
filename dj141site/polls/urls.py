from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # url(r'^$', 'dj14site.views.home', name='home'),
    # url(r'^dj14site/', include('dj14site.foo.urls')),
    #my_url
    url(r'^$', 'polls.views.home1'),
    url(r'^login/$', 'polls.views.login'),
    url(r'^login_auth/$', 'polls.views.login_auth'),
    url(r'^logout/$', 'polls.views.logout'),
    url(r'^thanks/$', 'polls.views.thanks'),
    url(r'^env/$', 'polls.views.env'),
    url(r'^home1/$', 'polls.views.home1'),
    url(r'^search1/$', 'polls.views.search1'),
    url(r'^result1/$', 'polls.views.result1'),
    url(r'^program1/$', 'polls.views.program1'),
    url(r'^about1/$', 'polls.views.about1'),
)
