from django import forms
from ..models import Account

class AccountActivateForm(forms.Form):
    amount = forms.DecimalField(label='Monto')

    class Meta:
        model = Account
        fields = ['amount']

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount < 10000:
            raise forms.ValidationError('El monto debe ser mayor a 10.000 COP')
        return amount
