from django.shortcuts import render
from .models import UserProfile

def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'administrator/user_list.html', {'users': users})

# administrator/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile

def delete_user(request, user_id):
    user_to_delete = get_object_or_404(UserProfile, id=user_id)

    if request.method == 'POST':
        user_to_delete.delete()
        return redirect('administrator:user_list')  # Redireciona para a lista de usuários após a exclusão

    return render(request, 'administrator/delete_user_confirm.html', {'user': user_to_delete})