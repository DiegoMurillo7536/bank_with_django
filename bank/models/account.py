from django.db import models
from .account_type import AccountType
from django.contrib.auth.models import User
from .user_profile import UserProfile

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=10, blank=True, null=True)
    is_exempt = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.account_name} - {self.amount}"

    def save(self, *args, **kwargs):
        if not self.pk:
            user = self.user_id
            try:
                user_profile = UserProfile.objects.get(user=user)
                first_letter = user.first_name[0] if user.first_name else ''
                last_letter = user.last_name[0] if user.last_name else ''
                id_numbers = user_profile.identificacion[:3] if user_profile.identificacion else ''
                self.account_name = f"{first_letter}{last_letter}{id_numbers}".upper()
            except UserProfile.DoesNotExist:
                raise ValueError("El usuario no tiene un perfil de usuario asociado.")
        super().save(*args, **kwargs)
        
    def top_account(self, amount,*args, **kwargs):
        self.amount += amount
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'bank_account'