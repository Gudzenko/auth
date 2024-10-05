from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username')


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email or Username', max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
