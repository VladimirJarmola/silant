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
    def clean(self):
        cleaned_data = super().clean()
        user_role = cleaned_data.get("user_role")
        service_company = cleaned_data.get("service_company")
        if user_role == "SE" and not service_company:
            msg = forms.ValidationError("Выберите из какой сервисной компании пользователь!", code="invalid")
            self.add_error("service_company", msg)

    class Meta:
        model = User
        fields = '__all__'

