from django.urls import path
from apps.badge.views import badge, admin, editUser

urlpatterns = [
    path('', badge, name = 'badge'),
    path('editUser/<int:user_id>', editUser, name = 'editUser'),
    path('admin/', admin, name = 'admin'),
]

