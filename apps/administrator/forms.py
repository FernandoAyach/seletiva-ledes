from django import forms
from .models import UserEditRequest

class UserEditRequestForm(forms.ModelForm):
    user = forms.IntegerField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = UserEditRequest
        fields = ('name','email','birth_date','phone','picture')      
        labels = {
            "name": "Nome",
            "email": "Email",
            "birth_date": "Data de nascimento",
            "phone": "Telefone",
            "picture": "Foto",
        }
        widgets = {
            "name": forms.TextInput(attrs = {"class": "input-form"}),
            "email": forms.TextInput(attrs = {"class": "input-form"}),
            "phone": forms.TextInput(attrs = {"class": "input-form"}),
            "picture": forms.FileInput(attrs = {"class": "input-form"}),
            "birth_date": forms.DateInput(
                attrs = {
                    "class": "input-form",
                    "type": "date"
                },
                format = "%Y-%m-%d",
            )
        }
