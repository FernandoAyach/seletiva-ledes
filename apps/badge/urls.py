from django.urls import path
from apps.badge.views import badge, editUser

urlpatterns = [
    path('', badge, name = 'badge'),
    path('editUser/', editUser, name = 'editUser'),
]
