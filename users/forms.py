from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ["username", "password"]

    username = forms.CharField()
    password = forms.CharField()


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = '__all__'

