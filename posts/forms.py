from django.forms import ModelForm
from django import forms
from posts.models import Post
from django.contrib.auth.models import User
from posts.models import UserProfile

class PostForm(ModelForm):
	class Meta:
		model = Post
		exclude = ('user_posting',) # so it will be taken as the current user and will not be displayed on the post submission form 
		
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('fav_color', 'location', 'date_of_birth')