from django.conf.urls import patterns, url

urlpatterns = patterns('jamhub.views',
	(r'^createProfile', 'create_profile'),
	(r'^logout', 'logout_view'),
	(r'^home', 'home'),
	(r'^profile', 'show_profile'),
	(r'^editProfile', 'edit_profile'),
	(r'^addProject', 'add_project'), 
	(r'^test', 'test'),
	
)