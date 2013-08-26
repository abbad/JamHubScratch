from django import forms

from jamhub.models import Profile, Role, Instrument, DAW

class ProfileForm(forms.ModelForm):
	role = forms.ModelMultipleChoiceField(queryset = Role.objects.all()) 
	instruments = forms.ModelMultipleChoiceField(queryset = Instrument.objects.all())
	software = forms.ModelMultipleChoiceField(queryset = DAW.objects.all())
	
	class Meta:
		model = Profile
		fields = ['user', 'role', 'instruments', 'software']
		exclude = ['user']