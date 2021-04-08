from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.models import post
from django.urls import reverse
from .models import profile as pro
from django.contrib.auth.models import User, models
from register.forms import signUpForm, updateUserForm, updateProfileForm
from django.views.generic import ListView

# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = signUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username} successfully')
			return redirect('/login')
	else:
		form = signUpForm()

	return render(request, 'register/signup.html', {'form': form} )

@login_required
def profile(request):

	if request.method == 'POST':
		u_form = updateUserForm(request.POST, instance=request.user)
		p_form = updateProfileForm(request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid:
			u_form.save()
			p_form.save()
			messages.success(request, f'Fieds updated successfully')
			return redirect('/profile')
	else:
		u_form = updateUserForm(instance=request.user)
		p_form = updateProfileForm(instance=request.user.profile)

	context = {
		'u_form' : u_form,
		'p_form' : p_form
	}
	
	return render(request, 'register/profile.html', context)
