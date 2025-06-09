from django import forms
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    class UserForm(forms.Form):
        name = forms.CharField()
        age = forms.IntegerField()