from django import forms
from .models import *
  
class storyForm(forms.ModelForm):
  
    class Meta:
        model = story
        fields = ['title', 'Img' , 'storytext']