from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
	name = models.CharField(max_length = 30) 
	
	def __unicode__(self):
		return self.name

class Instrument(models.Model):
	name = models.CharField(max_length = 30, unique = True)
	
	class Meta:
		ordering = ['name']
		
	def __unicode__(self):
		return self.name

class DAW(models.Model):
	name = models.CharField(max_length = 30, unique = True)
	
	class Meta: 
		ordering = ['name']
	
	def __unicode__(self):
		return self.name
		
class Profile(models.Model):
	user = models.ForeignKey(User)
	role = models.ManyToManyField(Role)
	instruments = models.ManyToManyField(Instrument)
	software = models.ManyToManyField(DAW)
	date_created = models.DateTimeField(auto_now_add = True)
	
	def __unicode__(self):
		return self.user
		
class Project(models.Model):
	artist = models.ManyToManyField(Profile)
	name = models.CharField(max_length = 30)
	num_stars = models.IntegerField()
	date_created = models.DateTimeField(auto_now_add = True)
	genre = models.CharField(max_length = 30)
	
	def __unicode__(self):
		return self.name