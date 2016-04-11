from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class ResearchnetAuthForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))

    error_messages = {
        'invalid_login': (
            "Please enter a correct %(username)s and password."
        ),
        'inactive': ("This account is inactive."),
    }