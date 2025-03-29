from django.contrib import admin
from bank.models.transaction import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount_in_transaction', 'id_from_account', 'id_to_account', 'id_transaction_type', 'created_at')
    search_fields = ('description',)