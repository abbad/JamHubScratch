from django import forms

from jamhub.models import Project, Profile, Role, Instrument, DAW 

class ProfileForm(forms.ModelForm):
	role = forms.ModelMultipleChoiceField(queryset = Role.objects.all()) 
	instruments = forms.ModelMultipleChoiceField(queryset = Instrument.objects.all())
	software = forms.ModelMultipleChoiceField(queryset = DAW.objects.all())
	
	class Meta:
		model = Profile
		fields = ['user', 'role', 'instruments', 'software']
		exclude = ['user']
		
class ProjectForm(forms.ModelForm):
	name = forms.CharField(max_length = 30)
	description = forms.CharField(max_length=300, widget=forms.Textarea)
	genre = forms.CharField(max_length = 30)
	
	class Meta:
		model = Project
		fields = ['name', 'genre', 'description']
		exclude = ['user', 'creator']