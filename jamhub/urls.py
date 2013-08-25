from django.conf.urls import patterns, url

urlpatterns = patterns('jamhub.views',
	(r'^logout', 'logout_view'),
	(r'^home', 'home'),
	(r'^test', 'test'),
    #(r'^sign$', 'create_musician'),
	#(r'^createProfile', 'create_profile_form'),
	#(r'^about', 'about'),
	#(r'^addProject', 'add_project'),
	#(r'^addInstrument', 'add_instrument'),
	#(r'^profile', 'show_profile'),
)