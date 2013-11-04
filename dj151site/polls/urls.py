from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from polls import views

# urlpatterns = patterns('',
#                        url(r'^$', views.index, name='index'),
#                        url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
#                        url(r'^(?P<poll_id>\d+)/result/$', views.results, name='results'),
#                        url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
#                        url(r'^latest\.html$', views.index),
#                        )
urlpatterns = patterns('',
                       url(r'^about$', TemplateView.as_view(template_name='polls/about.html'), name='about'),
                       url(r'^about2$', views.AboutView.as_view()),
                       url(r'^$', views.IndexView.as_view(), name="index"),
                       url(r'^about3$', views.MyView.as_view()),
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name="detail"),
                       url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name="results"),
                       url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
                       )
