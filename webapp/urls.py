from django.conf.urls import patterns, include, url
from django.contrib import admin
from webapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^event/(?P<event_name>[\w\-]+)/$', views.event, name='event'),
    url(r'^fan/(?P<username>[\w\-]+)/$', views.fan, name='fan'),
    url(r'^band/(?P<username>[\w\-]+)/$', views.band, name='band'),
    url(r'^wall/$', views.wall, name="wall"),
    url(r'^edit_profile/$', views.edit_profile, name="edit_profile"),
    url(r'^events/$', views.events, name='events'),
    url(r'^achievements/$', views.achievements, name="achievements"),
    url(r'^create_event', views.create_event, name='create_event'),
    url(r'^register/(?P<user_type>[\w\-]+)/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout')
)