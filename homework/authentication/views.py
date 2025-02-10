from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

from . import forms



def login_view(request):
    if request.user.is_authenticated:
        return redirect('quotes:main')
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect(to="quotes:main")
            else:
                form.add_error(None, 'Invalid username or password')
    return render(request, 'authentication/login.html', context={"form": form})



def sign_in(request):
    if request.user.is_authenticated:
        return redirect('quotes:main')
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Вітаємо {username}. Ваш акаунт успішно створено")
            return redirect(to="authentication:login")
        else:
            print("Form is not valid")
    return render(request, 'authentication/sign_up.html', context={"form": form})


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('quotes:main')
    auth_logout(request)
    return redirect('quotes:main')