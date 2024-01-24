from django.shortcuts import render, redirect
from apps.badge.models import BadgeUser
from apps.badge.forms import BadgeUserForms
from django.contrib import messages

def badge(request):
    badge_user = BadgeUser.objects.get(email = "teste@gmail.com")
    return render(request, 'badge/badge.html', { "user": badge_user})

def editUser(request, user_id):
    badge_user = BadgeUser.objects.get(id = user_id)
    form = BadgeUserForms(instance = badge_user)

    if request.method == "POST":
        form = BadgeUserForms(request.POST, request.FILES, instance = badge_user) 
            
        if form.is_valid():
            form.save()
            messages.success(request, "Fotografia editada!")
            return redirect("badge")

    return render(request, 'badge/editUser.html', {"form": form,  "user_id": user_id})
