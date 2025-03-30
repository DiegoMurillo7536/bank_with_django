from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms.registration_form import RegistrationForm
from django.core.exceptions import ValidationError
from .models import Account
# Create your views here.
@login_required
def bank(request):
    # Obtener todas las cuentas del usuario actual
    accounts = Account.objects.filter(user_id=request.user)
    
    context = {
        'accounts': accounts,
    }
    return render(request, 'bank/bank.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('bank')
            except ValidationError as e:
                form.add_error("identificacion", e.message)
    else:
        form = RegistrationForm()
    return render(request, 'bank/register.html', {'form': form})
