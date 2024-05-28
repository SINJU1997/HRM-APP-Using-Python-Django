# forms.py

from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {
            'name': '',
            'email': '',
            'password': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-sinju mandi', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'input-box', 'placeholder': 'Enter your email'}),
            'password': forms.PasswordInput(attrs={'class': 'input-box', 'placeholder': 'Enter your password'}),
        }
