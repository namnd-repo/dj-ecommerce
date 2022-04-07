from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
import re

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder': 'Enter username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder': 'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder': 'Confirm password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        # nam@gmail.com

        if not (re.fullmatch(regex, self.cleaned_data.get("email"))):
            raise forms.ValidationError('Invalid email ---- ʕ´•ᴥ•`ʔ')

        return self.cleaned_data.get("email")

