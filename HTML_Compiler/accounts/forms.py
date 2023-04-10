from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, FrontEnd

class RegisterForm(UserCreationForm):
	#password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
	username=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Enter Username'}), label='')
	first_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Enter First Name'}), label='')
	last_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Enter Last Name'}), label='')
	email=forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'Enter Email'}), label='')
	password1=forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}), label='')
	password2=forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}), label='')

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']
		#labels = {'email':'Email'}


class LoginForm(AuthenticationForm):
	username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Username'}), label='')
	password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}), label='')


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	first_name = forms.CharField()
	last_name = forms.CharField()

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['phone_number','profession', 'image']

class FrontEndForm(forms.ModelForm):
    class Meta:
        model=FrontEnd
        fields='__all__'