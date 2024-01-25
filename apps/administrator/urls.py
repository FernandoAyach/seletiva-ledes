from django.urls import path
from .views import user_edit_requests, approve_user_edit_request

app_name = 'admin_app'

urlpatterns = [
   path('user_edit_requests/', user_edit_requests, name='user_edit_requests'),
   path('approve_user_edit_request/<int:request_id>/', approve_user_edit_request, name='approve_user_edit_request'),
   
]
