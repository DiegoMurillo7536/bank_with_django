from django.contrib import admin

from bank.models.transaction_type import TransactionType

# Register your models here.
@admin.register(TransactionType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)