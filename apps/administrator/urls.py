from django.urls import path
from .views import reject_user_edit_request, user_edit_requests, approve_user_edit_request

app_name = 'administrator'

urlpatterns = [
   path('list/', user_edit_requests, name='list'),
   path('approve/<int:user_edit_request_id>/', approve_user_edit_request, name='approve'),
   path('reject/<int:user_edit_request_id>/', reject_user_edit_request, name='reject'),
]
