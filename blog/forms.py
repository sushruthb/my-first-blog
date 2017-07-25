'''
Created on Jul 25, 2017

@author: sbharat
'''
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','text',)