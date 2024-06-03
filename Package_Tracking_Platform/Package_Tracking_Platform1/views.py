from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.views.decorators.cache import never_cache

def landing_page(request):
    return render(request, 'landing_page.html', {'user': request.user})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@never_cache
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('landing_page')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@never_cache
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

@never_cache
@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

@never_cache
@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')
