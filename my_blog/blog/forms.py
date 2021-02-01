from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *


class SignUpForm(ModelForm):
#	first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
#	last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
#	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta:
		model = BlogUser
		exclude = ('is_editor', 'is_deactive')
        

# class SignUpForm(ModelForm):
# 	class Meta:
# 		model = BlogUser
# 		fields = ('__all__',)

class ArticleCreationForm(ModelForm):
	class Meta:
		model = Article
		fields = ('title', 'text', 'img_path', 'tag', 'topic')
