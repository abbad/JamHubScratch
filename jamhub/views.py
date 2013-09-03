# Django Http
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, Http404

# Friendship app 
from friendship.models import Friend, Follow

# my models 
from forms import ProfileForm, ProjectForm
from models import Profile, Project

def home(request):
	projects = Project.objects.all().order_by('-date_created')[:10]
	return render(request, 'home.html', {'projects' : projects})
	
def logout_view(request):
	logout(request)
	return redirect('home.html')

def create_profile(request):
	# REMEMBER TO HANDLE UNAUTHENTICATED USERS
	if request.method == 'POST':
		profileForm = ProfileForm(request.POST)
		if profileForm.is_valid() and request.user.is_authenticated():
			profile = profileForm.save(commit = False)
			profile.user = request.user
			profile.is_active = True
			profile.save()
			profileForm.save_m2m()
			return HttpResponseRedirect('home.html')
		else:
			return render(request, 'createProfile.html', {'form': profileForm})
	else:
		profileForm = ProfileForm()
		return render(request, 'createProfile.html', {'form': profileForm})

def edit_profile(request):
	profile = Profile.objects.get(user = request.user) 
	if request.method == 'POST':
		profileForm = ProfileForm(request.POST, instance = profile)
		if profileForm.is_valid() and request.user.is_authenticated():
			profile = profileForm.save(commit = False)
			profile.user = request.user
			profile.is_active = True
			profile.save()
			profileForm.save_m2m()
			return HttpResponseRedirect('home.html')
		else:
			return render(request, 'editProfile.html', {'profileForm': profileForm})
	else:
		profileForm = ProfileForm(instance = profile)
		return render(request, 'editProfile.html', {'profileForm': profileForm})
	
def add_project(request):
	# REMEMBER TO HANDLE UNAUTHENTICATED USERS
	if request.method == 'POST':
		projectForm = ProjectForm(request.POST)
		if projectForm.is_valid() and request.user.is_authenticated():
			project = projectForm.save(commit = False) 
			project.creator = request.user
			project.is_active = True
			project.save()
			projectForm.save_m2m()
			return HttpResponseRedirect('profile')
		else: 
			return render(request, 'addProject.html', {'projectForm': projectForm})
	else: 
		projectForm = ProjectForm()
		return render(request, 'addProject.html', {'projectForm': projectForm})
			
def show_profile(request):
	# get profile related to user. 
	profile = Profile.objects.get(user = request.user)
	# get list of projects he created 
	projects = Project.objects.filter(creator = request.user) 
	return render(request, 'profile.html', { 'profile' : profile, 'projects' : projects})

def show_project(request, project_id):
	if not request.user.is_authenticated(): 
		return render(request, 'test.html')
	
	# get the object 
	try:
		project = Project.objects.get(id = project_id)
	except :
		raise Http404
	
	return render(request, 'showProject.html', {'project' : project})
		
def test(request):
	return render(request, 'test.html')
	