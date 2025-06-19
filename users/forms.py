from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserForm(forms.ModelForm):
    class UserForm(forms.Form):
        name = forms.CharField()
        age = forms.IntegerField()