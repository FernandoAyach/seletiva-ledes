from django.shortcuts import render, redirect
from apps.badge.models import BadgeUser
from apps.badge.forms import BadgeUserForms
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def badge(request):
    badge_user = BadgeUser.objects.get(id = 2)
    return render(request, 'badge/badge.html', { "user": badge_user})

def editUser(request, user_id):
    badge_user = BadgeUser.objects.get(id = user_id)
   
    if request.method == "POST":
        form = BadgeUserForms(request.POST, request.FILES, instance = badge_user) 
            
        if form.is_valid():
            form.save()
            messages.success(request, "Fotografia editada!")
            return redirect("badge")
        print("erro: ", form.errors)
    else:
        form = BadgeUserForms(instance = badge_user)

    return render(request, 'badge/editUser.html', {"form": form,  "user_id": user_id})

@login_required(login_url='login')
def admin(request):
    """
    badge_user = request.user

    if not badge_user.is_admin:
        return redirect('badge')

    user2 = BadgeUser.objects.get(id=7)
    alteracao = [
        {
            'user': user2, 
            'new_data': {
                'name': 'gasparzinho', 
                'email': 'gaspart@zin.com', 
                'birth_date': '06 de Setembro de 2019', 
                'phone': '(67) 4002-8922',
                'picture': badge_user.picture,
            }
        },
        {
            'user': badge_user, 
            'new_data': {
                'name': '',
                'email': '',
                'birth_date': '',
                'phone': '',
                'picture': '',
            }
        },
    ]
    """
    return render(request, 'badge/admin.html', {'alteracao': {}})
