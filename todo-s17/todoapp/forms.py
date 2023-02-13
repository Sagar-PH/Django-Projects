from .models import Todo
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TodoForm(ModelForm):
    class Meta:
        model=Todo
        fields='__all__'
    
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']