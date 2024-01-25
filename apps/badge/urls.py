from django.urls import path
from apps.badge.views import badge

urlpatterns = [
    path('', badge, name = 'badge'),
]