from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from . forms import CreateUserForm, LoginForm

def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('badge')

    return render(request, 'authentication/login.html', context={'login_form': form})


@login_required(login_url='login')
def create_user(request):
    if not request.user.is_admin:
        return HttpResponse('Access denied.')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    return render(request, 'authentication/create-user.html', context={'register_form': form})


@login_required(login_url='login')
def dashboard(request):
    if request.user.is_admin:
        return HttpResponse('you\'re an admin!')

    return render(request, 'authentication/dashboard.html')


def user_logout(request):
    auth.logout(request)
    return redirect('/')
