from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import AbstractUser
from .models import Profile



class Signupform(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class meta:
        model = AbstractUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class Editprofileform(UserChangeForm):
    class meta:
        model = AbstractUser        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'logo']
        

class CustomPasswordChangeForm(PasswordChangeForm):
    pass              