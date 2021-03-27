from django import forms
from .models import *
from django.contrib.auth.models import User
  
class storyForm(forms.ModelForm):
    class Meta:
        model = story
        fields = ['title', 'Img' , 'storytext']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    username = forms.CharField(widget=forms.TextInput,label='Username')

    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password')