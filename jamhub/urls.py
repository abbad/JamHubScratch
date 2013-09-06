from django.conf.urls import patterns, url

urlpatterns = patterns('jamhub.views',
	(r'^createProfile', 'create_profile'),
	(r'^logout', 'logout_view'),
	(r'^home', 'home'),
	(r'^addProject', 'add_project'), 
	(r'^profile/(?P<user_name>[\w\-.]+)', 'show_profile'),
	(r'^editProfile', 'edit_profile'),
	(r'^projects/(?P<project_id>\d+)', 'show_project'),
	(r'^editProject/(?P<project_id>\d+)$', 'edit_project'),
	(r'^test', 'test'),
	
)