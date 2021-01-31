from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import BlogUser


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
	last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        

# class SignUpForm(ModelForm):
# 	class Meta:
# 		model = BlogUser
# 		fields = ('__all__',)

