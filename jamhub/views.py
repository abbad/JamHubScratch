# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

from forms import ProfileForm

def home(request):
    return render(request, 'home.html')
	
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
	
def test(request):
	return render(request, 'test.html')
	
