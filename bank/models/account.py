from django.db import models
from .account_type import AccountType
from django.contrib.auth.models import User

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=10, blank=False, null=False)  # Iniciales del cliente
    is_exempt = models.BooleanField(default=False)  # Exento de impuestos o algo similar
    user_id = models.IntegerField()  # ID del cliente como entero
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)  # Relación con tipo de cuenta
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Saldo de la cuenta
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Última actualización

    def __str__(self):
        return f"{self.account_name} - {self.amount}"

    class Meta:
        db_table = 'bank_account'