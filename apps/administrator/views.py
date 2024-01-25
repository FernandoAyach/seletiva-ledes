from django.shortcuts import render, get_object_or_404, redirect
from .models import UserEditRequest
from .forms import UserEditRequestForm

def user_edit_requests(request):
    requests = UserEditRequest.objects.filter(is_approved=False)
    return render(request, 'admin_app/user_edit_requests.html', {'requests': requests})

def approve_user_edit_request(request, request_id):
    user_edit_request = get_object_or_404(UserEditRequest, id=request_id)
    if request.method == 'POST':
        form = UserEditRequestForm(request.POST, instance=user_edit_request)
        if form.is_valid():
            form.save()
            user_edit_request.approve()
            # Implemente a lógica para aprovar a solicitação e atualizar as informações do usuário
            return redirect('admin_app:user_edit_requests')
    else:
        form = UserEditRequestForm(instance=user_edit_request)

    return render(request, 'admin_app/approve_user_edit_request.html', {'form': form})
