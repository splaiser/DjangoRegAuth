from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm
from .forms import RegisterForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            country = form.cleaned_data.get('country')
            user = authenticate(username=username, password=raw_password)

            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})

def register(request):
    form = RegisterForm
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        #check the validation of this form
        if registerForm.is_valid():
            registerForm.save()
            messages.success(request, 'Registration completed !')
            return redirect('register')
    return render(request, 'register.html', {'form': form})
