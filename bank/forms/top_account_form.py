from django import forms
from ..models import Account

class TopAccountForm(forms.Form):
    def __init__(self, account_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        account = Account.objects.get(id=account_id)  # Obtener la cuenta
        self.fields['account'] = forms.CharField(
            initial=account.account_name,
            label='Cuenta',
            widget=forms.TextInput(attrs={
                'readonly': 'readonly',
                'class': 'form-control'
            })
        )
    
    amount = forms.IntegerField(label='Cantidad')
    class Meta:
        model = Account
        fields = ['account', 'amount', 'is_active']
        
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 10000:
            raise forms.ValidationError('El monto debe ser mayor a 10.000 COP')
        return amount
    
    def clean_is_active(self):
        is_active = self.cleaned_data['is_active']
        if not is_active:
            raise forms.ValidationError('La cuenta debe estar activa')
        return is_active
    
