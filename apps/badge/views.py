from django.shortcuts import render, redirect
from apps.authentication.models import BadgeUser
from apps.badge.forms import BadgeUserForms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.administrator.forms import UserEditRequestForm

@login_required(login_url='login')
def badge(request):
    badge_user = request.user
    return render(request, 'badge/badge.html', { "user": badge_user})

@login_required(login_url='login')
def editUser(request):
    if request.method == "POST":
        form = UserEditRequestForm(request.POST, request.FILES) 
            
        if form.is_valid():
            userEditRequest = form.save(commit=False)
            userEditRequest.user = request.user
            userEditRequest.save()
            messages.info(request, "Sua atualização de conta foi mandada para aprovação!")
            return redirect("badge")
    else:
        form = UserEditRequestForm(instance=request.user)

    return render(request, 'badge/editUser.html', {"form": form})
