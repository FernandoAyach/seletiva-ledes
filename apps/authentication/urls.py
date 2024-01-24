from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('create-user/', views.create_user, name='register'),
    path('logout/', views.user_logout, name='logout'),
]
