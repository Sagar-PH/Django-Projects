
from django.forms import ModelForm
from .models import Thread
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ThreadForm(ModelForm):
    class Meta:
        model=Thread
        fields='__all__'

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
