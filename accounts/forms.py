from django import forms
from .models import User
''', Profile'''
from django.contrib.auth.forms import UserCreationForm


class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100, label="Last Name")
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password1', 'password2']


class StudentUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100, label="Last Name")
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image', 'testimonial', 'phone_number']
