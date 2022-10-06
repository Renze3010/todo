from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        
class CustomLoginForm(AuthenticationForm):


    username = forms.CharField(label="", widget=TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="", widget=PasswordInput(attrs={'placeholder':'Password'}))