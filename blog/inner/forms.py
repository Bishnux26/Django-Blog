from django import forms
from .models import Blog, Comment
from django.contrib.auth.models import User

class EditProfile(forms.ModelForm):
    widgets={'username':forms.TextInput(attrs={'class': 'form-control'})}
    class Meta:
        model=User
        widgets={'username':forms.TextInput(attrs={'class': 'form-control'}),
                 'first_name':forms.TextInput(attrs={'class': 'form-control'}),
                 'last_name':forms.TextInput(attrs={'class': 'form-control'}),
                 'email':forms.TextInput(attrs={'class': 'form-control'})}
        fields=['username','first_name','last_name','email']
        
class Blogs(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','description','images']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control','id':'dex'}),
        }