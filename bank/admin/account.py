from django.contrib import admin
from ..models import Account
from ..models.user_profile import UserProfile
from django.contrib.auth.models import User

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_name', 'user_id', 'account_type', 'amount', 'is_exempt', 'created_at')
    search_fields = ('account_name',)
    list_filter = ('is_exempt', 'account_type')
    readonly_fields = ('amount', 'account_name')