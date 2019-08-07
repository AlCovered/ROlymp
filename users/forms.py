from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from .models import *


class UserRegistration(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2']

    def clean_username(self):
        new_username = self.cleaned_data['username'].lower()
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890_.@'
        point = False

        for element in new_username:
            if element not in chars:
                point = True

        if point:
            raise ValidationError(f'"{new_username}" - неправильное имя пользователя')

        return new_username

    def clean_email(self):
        new_email = self.cleaned_data['email'].lower()

        if (new_email.startswith('example')) or (not (new_email.endswith('ru') or new_email.endswith('com') or new_email.endswith('net') or new_email.endswith('ua'))) or (not('gmail' in new_email or 'email' in new_email or 'mail' in new_email or 'ukr' in new_email)):
            raise ValidationError('Введите корректный адрес электронной почты')

        return new_email


class UpdateProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']


class EditImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']
