from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def signup(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
	else:
		form = UserCreationForm()

	return render(request, 'register/signup.html', {'signupform': form} )
