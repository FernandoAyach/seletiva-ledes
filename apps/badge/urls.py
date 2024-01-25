from django.urls import path
from apps.badge.views import badge, admin

urlpatterns = [
    path('', badge, name = 'badge'),
    path('admin/', admin, name = 'admin'),
]
