from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	user_posting = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.title	
	
class UserProfile(models.Model):
	# This line is required. Links UserProfile to a User model instance.#
	user = models.OneToOneField(User)
	# The additional attributes we wish to include.#
	fav_color = models.CharField(max_length=25, blank=True) #could create another table with colors, maybe next time ....#
	location = models.CharField(max_length=200, blank=True) #could create another table with locations or at least some more structire location with street, city, state etc, but maybe next time ....#
	date_of_birth  = models.DateField(blank=True)

	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
		return self.user.username