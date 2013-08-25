# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')
	
def logout_view(request):
	logout(request)
	return redirect('home.html')

def create_profile(request):
	return render(request, 'createProfile.html')
	
def test(request):
	return render(request, 'test.html')
	
