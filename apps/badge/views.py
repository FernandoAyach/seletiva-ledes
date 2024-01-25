from django.shortcuts import render
from apps.authentication.models import BadgeUser
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def badge(request):
    badge_user = request.user
    return render(request, 'badge/badge.html', { "user": badge_user} )
