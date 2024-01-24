from django import forms

from apps.badge.models import BadgeUser

class BadgeUserForms(forms.ModelForm):
    class Meta: 
        model = BadgeUser
        exclude = ["password", "last_login", "groups", "user_permissions", "is_admin", "validity_date"]
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