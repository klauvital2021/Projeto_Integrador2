from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ResponsavelPrincipalForm(UserCreationForm):
    first_name = forms.CharField(
        label='Nome',
        max_length=150,
    )
    last_name = forms.CharField(
        label='Sobrenome',
        max_length=150,
    )
    email = forms.EmailField(
        label='E-mail',
    )
    password1 = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmação da Senha')   # noqa E501

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
