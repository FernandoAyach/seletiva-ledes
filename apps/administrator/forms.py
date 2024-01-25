from django import forms
from .models import UserEditRequest

class UserEditRequestForm(forms.ModelForm):
    user = forms.IntegerField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = UserEditRequest
        fields = ('name','email','birth_date','phone','picture')
