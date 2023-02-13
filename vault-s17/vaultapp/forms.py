from django.forms import ModelForm
from .models import Vault
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VaultForm(ModelForm):
    class Meta:
        model=Vault
        fields='__all__'

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']