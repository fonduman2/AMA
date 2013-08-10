from django.conf.urls import patterns, include, url

from home.views import index

urlpatterns = patterns('',
	url(r'^$', index, name="index"),
)