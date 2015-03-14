from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin
from webapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'discoveragig.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('webapp.urls')),
    url(r'^register/(?P<user_type>[\w\-]+)/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout')

)