from django import forms
from ..models import Transaction, Account, TransactionType

class MakeTransactionForm(forms.Form):
    def __init__(self, user_id = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['account_from'].queryset = Account.objects.filter(user_id=user_id)

    
    account_from = forms.ModelChoiceField(
        queryset=Account.objects.none(), 
        label='Cuenta Origen',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    account_to = forms.ModelChoiceField(
        queryset=Account.objects.all(), 
        label='Cuenta Destino',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    amount = forms.IntegerField(label='Cantidad')
    description = forms.CharField(label='Descripción', max_length=100)
    transaction_type = forms.ModelChoiceField(queryset=TransactionType.objects.all(), label='Tipo de Transacción')
    
    
    class Meta:
        model = Transaction
        fields = ['account_from', 'account_to']
        
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 10000:
            raise forms.ValidationError('El monto debe ser mayor a 10.000 COP')
        return amount