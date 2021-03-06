from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rssreader.views.home', name='home'),
    # url(r'^rssreader/', include('rssreader.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rssfeedreader/', include('rssfeedreader.urls')),
    
    # Allows the rssfeedreader view/template to be the index page.
    url(r'^$', include('rssfeedreader.urls')),
)
