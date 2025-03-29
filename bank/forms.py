from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models.user_profile import UserProfile
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    identificacion = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        
        # Verificar si la identificación ya existe
        identificacion = self.cleaned_data["identificacion"]
        if UserProfile.objects.filter(identificacion=identificacion).exists():
            raise ValidationError("Ya existe un usuario con esta identificación")
        
        if commit:
            user.save()
            # Crear el perfil de usuario con la identificación
            UserProfile.objects.create(
                user=user,
                identificacion=identificacion
            )
        return user