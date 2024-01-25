from django.urls import path
from .views import user_edit_requests, new_user_edit_request, approve_user_edit_request

app_name = 'administrator'

urlpatterns = [
   path('list/', user_edit_requests, name='list'),
   path('new/', new_user_edit_request, name='new'),
   path('approve/<int:user_edit_request_id>/', approve_user_edit_request, name='approve'),
]
