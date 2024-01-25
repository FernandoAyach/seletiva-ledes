from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput

from .models import BadgeUser

class CreateUserForm(UserCreationForm):
    class Meta:
        model = BadgeUser
        fields = ['name', 'email', 'birth_date', 'phone', 'validity_date', 'picture']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control'}))