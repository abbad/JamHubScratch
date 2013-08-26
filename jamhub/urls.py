from django.conf.urls import patterns, url

urlpatterns = patterns('jamhub.views',
	(r'^createProfile', 'create_profile'),
	(r'^logout', 'logout_view'),
	(r'^home', 'home'),
	(r'^showProfile', 'show_profile'),
	(r'^test', 'test'),
	
)