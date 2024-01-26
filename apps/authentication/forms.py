from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget = TextInput(
            attrs={
                'class': "input-form",
                "placeholder": "joaosilva@gmail.com"
            }
        )
    )
    password = forms.CharField(
        label = "Senha",
        widget = PasswordInput(
            attrs={
                'class': "input-form",
                "placeholder": "********"
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')

        try:
            validate_email(username)
        except ValidationError:
            raise forms.ValidationError('Por favor, insira um endereço de e-mail válido.')
        
        self.errors.pop('username', None)

        return username
        
