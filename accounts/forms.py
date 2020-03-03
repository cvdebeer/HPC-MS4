from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100, label="Last Name")
    username = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'password1', 'password2']
