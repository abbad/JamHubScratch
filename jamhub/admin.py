from jamhub.models import Profile, DAW, Instrument, Role, Project
from django.contrib import admin
from django.contrib.sessions.models import Session

admin.site.register(Session)
admin.site.register(Profile) 
admin.site.register(DAW) 
admin.site.register(Role)
admin.site.register(Instrument)