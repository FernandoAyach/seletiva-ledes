from django.shortcuts import render, get_object_or_404, redirect
from .models import UserEditRequest
from .forms import UserEditRequestForm

def user_edit_requests(request):
    alteracoes = UserEditRequest.objects.filter(is_approved=False,is_rejected=False)
    return render(request, 'administrator/list.html', {'alteracao': alteracoes})



def new_user_edit_request(request):
    form = UserEditRequestForm()

    if request.method == 'POST':
        data = {
            'user': request.user.id,
            'name': request.POST['name'],
            'email': request.POST['email'],
            'birth_date': request.POST['birth_date'],
            'phone': request.POST['phone'],
            'is_approved': False,
        }

        print(request.POST)

        form = UserEditRequestForm(data, request.FILES)
        if form.is_valid():
            userEditRequest = form.save(commit=False)
            userEditRequest.user = request.user
            userEditRequest.save()

    return render(request, 'administrator/new.html', {'form': form})



def approve_user_edit_request(request, user_edit_request_id):
    user_edit_request = get_object_or_404(UserEditRequest, id=user_edit_request_id)

    if request.method == 'POST':
        user_edit_request.approve()
        return redirect('administrator:list')
    
    return redirect('/')


def reject_user_edit_request(request, user_edit_request_id):
    user_edit_request = get_object_or_404(UserEditRequest, id=user_edit_request_id)

    if request.method == 'POST':
        user_edit_request.reject()
        print( 'Solicitação de edição rejeitada com sucesso.')
        return redirect('administrator:list')
    
    return redirect('/')

