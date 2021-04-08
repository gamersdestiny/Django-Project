from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from register.models import profile

class signUpForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email', 'password1', 'password2']

class updateUserForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields =['username', 'email']

class updateProfileForm(forms.ModelForm):
	class Meta:
		model = profile
		fields = ['image']