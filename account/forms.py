from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SingUpForm(UserCreationForm):
    
    password2 = forms.CharField(
        label="confirm Password (again)", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("username", "email")
        lables = {"email": "Email"}
