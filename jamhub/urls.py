from django.conf.urls import include, patterns, url

urlpatterns = patterns('jamhub.views',
	(r'^createProfile', 'create_profile'),
	(r'^logout'								, 'logout_view'),
	(r'^home'								, 'home'),
	(r'^profile/(?P<user_name>[\w\-.]+)'	, 'show_profile'),
	(r'^editProfile'						, 'edit_profile'),
	(r'^projects/(?P<project_id>\d+)'		, 'show_project'),
	(r'^editProject/(?P<project_id>\d+)$'	, 'edit_project'),
	(r'^addProject'							, 'add_project'), 
	(r'^deleteProject/(?P<project_id>\d+)$'	, 'delete_project'),
	(r'^search/'							, include('haystack.urls')),
	(r'^test', 'test'),
	
)