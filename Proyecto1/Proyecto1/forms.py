from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    pass
