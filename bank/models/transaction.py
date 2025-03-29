from django.db import models
from bank.models.account import Account
from bank.models.transaction_type import TransactionType

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    amount_in_transaction = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    id_from_account = models.ForeignKey(Account, related_name='sent_transactions', on_delete=models.CASCADE)
    id_to_account = models.ForeignKey(Account, related_name='received_transactions', on_delete=models.CASCADE)
    id_transaction_type = models.ForeignKey('TransactionType', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """ Actualiza los saldos de las cuentas al guardar una transacción """
        if self.id_from_account.amount >= self.amount_in_transaction:
            self.id_from_account.amount -= self.amount_in_transaction
            self.id_to_account.amount += self.amount_in_transaction
            self.id_from_account.save()
            self.id_to_account.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("Saldo insuficiente en la cuenta de origen")

    class Meta:
        db_table = 'bank_transaction'

    def __str__(self):
        return f"Transaction {self.id} - {self.amount_in_transaction}"