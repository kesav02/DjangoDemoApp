from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'posts.views.index'),
	url(r'^post/$', 'posts.views.post'),
	url(r'^user_profile/$', 'posts.views.user_profile'),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}),
)
