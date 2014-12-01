from django.conf.urls import patterns, include, url
from blog.views import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'koala.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index),
    #url(r'^blog/index/$',index),
    #url(r'^blog/show_book/$',show_book),
    #url(r'^blog/register/$',register),
    url(r'^regist/$',regist),
    url(r'^login/$',login),
    url(r'^index/$',index),
    url(r'^logout/$',logout),
    url(r'^blog/$',blog),
)
