
from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
                       # url(r'^$', 'dj14site.views.home', name='home'),
                       # url(r'^dj14site/', include('dj14site.foo.urls')),
                       #my_url
                       url(r'^$', 'welcome'),
                       url(r'^index/$', 'index'),
                       url(r'^welcome/$', 'welcome', name='welcome'),
                       url(r'^login/$', 'login', name='login'),
                       url(r'^logout/$', 'logout', name='logout'),
                       url(r'^list/$', 'blog_list', name='bloglist'),
                       url(r'^(?P<id>\d+)/$', 'blog_detail', name='blogdetail'),
                       url(r'^add/$', 'blog_add', name='blogadd'),
                       url(r'^authoradd/$', 'author_add', name='author_add'),
                       url(r'^del/$', 'blog_del', name='blogdel'),
                       url(r'^update/$', 'blog_update', name='blogupdate'),
                       url(r'^admin/$', 'admin', name="blogadmin"),
                       url(r'^validate/$', 'validate', name='validate'),
                       url(r'^now/$', 'current_now', name="now"),
                       url(r'^test/$', 'test'),
                       url(r'test_css/$', 'test_css'),
                       url(r'testjs/(?P<template_name>\w+)?$', 'test_js'),
                       )
