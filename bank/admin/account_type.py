from django.contrib import admin

from bank.models.account_type import AccountType

# Register your models here.
@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)