from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from . forms import LoginForm

def login(request):
    if request.user.is_authenticated:
        return redirect('badge') if not request.user.is_admin else redirect('admin')

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            email = request.POST.get('username')
            user_password = request.POST.get('password')

            user = authenticate(request, username=email, password=user_password)
           
            if user is not None:
                auth.login(request, user)
                return redirect('badge')

    return render(request, 'authentication/login.html', context={'login_form': form})

def user_logout(request):
    auth.logout(request)
    return redirect('login')
