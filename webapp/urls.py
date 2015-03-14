from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin
from webapp import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)