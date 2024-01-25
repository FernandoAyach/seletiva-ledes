from django.shortcuts import render
from apps.badge.models import BadgeUser

def badge(request):
    badge_user = BadgeUser.objects.get(email = "teste@gmail.com")
    return render(request, 'badge/badge.html', { "user": badge_user} )
