from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import RegistrationForm
from django.core.exceptions import ValidationError
# Create your views here.
@login_required
def bank(request):
    return render(request, 'bank/bank.html')

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
