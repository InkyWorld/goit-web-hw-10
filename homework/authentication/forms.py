from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, TextInput, EmailInput, EmailField, PasswordInput

class RegisterForm(UserCreationForm):
    username = CharField(
        label='Username',
        max_length=15, 
        min_length=3,
        required=True,
        widget=TextInput(attrs={'class': 'form-control', "id": "InputUsername"}),
    )
    email = EmailField(
        label='Email',
        required=True,
        widget=EmailInput(attrs={'class': 'form-control', "id": "InputEmail"})
    )
    password1 = CharField(
        label='Password',
        required=True,
        widget=PasswordInput(attrs={'class': 'form-control', "id": "InputPassword1"})
    )
    password2 = CharField(
        label='Confirm',
        required=True,
        widget=PasswordInput(attrs={'class': 'form-control', "id": "InputPassword2"})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class LoginForm(AuthenticationForm):
    username = CharField(
        label='Username',
        max_length=15,
        min_length=3,
        required=True,
        widget=TextInput(attrs={'class': 'form-control', "id": "InputUsername"})
    )
    password = CharField(
        label='Password',
        required=True,
        widget=PasswordInput(attrs={'class': 'form-control', "id": "InputPassword"})
    )

    class Meta:
        model = User
        fields = ('username', 'password')