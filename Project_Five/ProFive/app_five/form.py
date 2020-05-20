from django import forms
from django.db import models
from app_five.models import UserProfileInfo
from django.contrib.auth.models import User
from django.forms import ModelForm



#form for the base class, just getting the password and hashing it
class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','email','password']


#this is the class for the user

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=['portofolio_site','profile_pic']
