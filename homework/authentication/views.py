from django.shortcuts import redirect, render

from . import forms
# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from . import forms

from django.contrib.auth.models import User

def login_view(request):
    form = forms.LoginForm()

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        print('POST request received')
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f'Username: {username}, Password: {password}')
            
            user = authenticate(request, username=username, password=password)
            print(f'User from authenticate: {user}')
            
            if user is not None:
                login(request, user)
                print(f'Logged in as: {user.username}')
                return redirect(to="quotes:main")
            else:
                print('Invalid username or password')
                form.add_error(None, 'Invalid username or password')
        else:
            print('Form is not valid ', form.errors)
            print(form.error_messages)
    
    return render(request, 'authentication/login.html', context={"form": form})



def sign_in(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        print("Form submitted")
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="authentication:login")
        else:
            print("Form is not valid")
            print(form.errors)
    return render(request, 'authentication/sign_in.html', context={"form": form})

def logout(request):
    return render(request, 'authentication/logout.html', context={})