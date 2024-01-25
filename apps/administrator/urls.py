from django.urls import path
from .views import delete_user, user_list

app_name = 'administrator'

urlpatterns = [
    path('<int:user_id>/delete/', delete_user, name='delete_user'),
    path('user-list/', user_list, name='user_list'),
]
