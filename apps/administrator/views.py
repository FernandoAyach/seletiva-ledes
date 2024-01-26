from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserEditRequest
from .forms import UserEditRequestForm

@login_required(login_url='login')
def user_edit_requests(request):
    if not request.user.is_admin:
        return redirect("/")
    
    alteracoes = UserEditRequest.objects.filter(is_approved=False,is_rejected=False)
    return render(request, 'administrator/list.html', {'alteracao': alteracoes})

@login_required(login_url='login')
def approve_user_edit_request(request, user_edit_request_id):
    if not request.user.is_admin:
        return redirect("/")
    
    user_edit_request = get_object_or_404(UserEditRequest, id=user_edit_request_id)

    if request.method == 'POST':
        user_edit_request.approve()
        return redirect('administrator:list')
    
    return redirect('/')

@login_required(login_url='login')
def reject_user_edit_request(request, user_edit_request_id):
    if not request.user.is_admin:
        return redirect("/")
    
    user_edit_request = get_object_or_404(UserEditRequest, id=user_edit_request_id)

    if request.method == 'POST':
        user_edit_request.reject()
        print( 'Solicitação de edição rejeitada com sucesso.')
        return redirect('administrator:list')
    
    return redirect('/')

