from django import forms

from el_mundo.models import Languages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LanguagesForm(forms.Form):
    languages = forms.ModelChoiceField(queryset=Languages.objects.all().order_by('name'))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



