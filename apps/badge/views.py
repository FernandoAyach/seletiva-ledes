from django.shortcuts import render, redirect
from apps.authentication.models import BadgeUser
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def badge(request):
    badge_user = request.user
    return render(request, 'badge/badge.html', { "user": badge_user} )

@login_required(login_url='login')
def admin(request):
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

    return render(request, 'badge/admin.html', {'alteracao': alteracao})

