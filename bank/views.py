from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms.registration_form import RegistrationForm
from django.core.exceptions import ValidationError
from .models import Account
from .forms.account_activate_form import AccountActivateForm
from .forms.make_transaction_form import MakeTransactionForm
from django.contrib import messages
from .models import Transaction
from .forms.top_account_form import TopAccountForm
# Create your views here.
@login_required
def bank(request):
    accounts = Account.objects.filter(user_id=request.user)
    form = MakeTransactionForm(request.user)
    context = {
        'accounts': accounts,
        'form': form,
    }
    return render(request, 'bank/bank.html', context)

def logout_view(request):
    logout(request)
    return redirect('bank:index')

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

def go_to_activate_account(request, account_id):
    account = Account.objects.get(id=account_id)
    if request.method == 'POST':
        form = AccountActivateForm(request.POST)
        if form.is_valid():
            account.amount = form.cleaned_data['amount']
            account.is_active = True
            account.save()
            return redirect('bank:index')
    else:
        form = AccountActivateForm()
    return render(request, 'bank/account/activate_account.html', {'form': form})

def make_transaction(request):
    
    if request.method == 'POST':
        form = MakeTransactionForm(request.user, request.POST)
        if form.is_valid():
            transaction = Transaction(
                amount_in_transaction=form.cleaned_data['amount'],
                description=form.cleaned_data['description'],
                id_from_account=form.cleaned_data['account_from'],
                id_to_account=form.cleaned_data['account_to'],
                id_transaction_type=form.cleaned_data['transaction_type']
            )
            transaction.save()
            messages.success(request, 'Transacción realizada correctamente')
    return redirect('bank:index', messages=messages)

def top_account(request, account_id):
    account = Account.objects.get(id=account_id)
    if request.method == 'POST':
        form = TopAccountForm(account_id, request.POST)
        if form.is_valid():
            account.amount = form.cleaned_data['amount']
            account.save()
            messages.success(request, 'Cuenta topada correctamente')
            return redirect('bank:index')
    else:
        form = TopAccountForm(account_id)
        return render(request, 'bank/account/top_account.html', {'form': form})
