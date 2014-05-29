from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}), #this will take you back to the login screen, did not implement any fency tank you message ...#
	url(r'', include('posts.urls')),#deligate all URLs to the post app
)
