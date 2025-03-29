from django.contrib import admin
from bank.models.account import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_name', 'user_id', 'account_type', 'amount', 'is_exempt', 'created_at')
    search_fields = ('account_name',)
    list_filter = ('is_exempt', 'account_type')