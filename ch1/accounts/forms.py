from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control my-2',
            'value': "",
            'required autofocus': True,
            'autocomplete': 'off',
        }
    ))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'type': 'password',
                'class': 'form-control my-2',
                'name': 'password',
                'required data-eye': True,
                'autocomplete': 'off',
            }
        ),
    )