from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from register.forms import signUpForm

# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = signUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'account created for {username} successfully')
			return redirect('/')
	else:
		form = signUpForm()

	return render(request, 'register/signup.html', {'form': form} )
@login_required
def profile(request):
	return render(request, 'register/profile.html')
