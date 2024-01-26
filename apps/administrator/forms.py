from django import forms
from .models import UserEditRequest
import re

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
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        phone_pattern = re.compile(r'^\(\d{2}\) \d{5}-\d{4}$')

        if not phone_pattern.match(phone):
            raise forms.ValidationError("Telefone inválido")

        return phone
