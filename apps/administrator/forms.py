from django import forms
from .models import UserEditRequest

class UserEditRequestForm(forms.ModelForm):
    class Meta:
        model = UserEditRequest
        fields = '__all__'