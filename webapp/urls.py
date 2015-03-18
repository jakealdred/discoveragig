from django.conf.urls import patterns, include, url
from django.contrib import admin
from webapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/(?P<user_type>[\w\-]+)/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout')
)