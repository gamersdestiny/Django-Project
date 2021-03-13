from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import post, Threads
# Create your views here.

def home(request):
	context={
	'dicpost': post.objects.all(),
	'dicThreads': Threads.objects.all()
	}
	return render(request, 'blog/bloghome.html', context)

def about(request):
	return render(request, 'blog/blogabout.html', {'title':'BlogAbout'})

def contact(request):
	return render(request, "blog/blogcontact.html", {'title': 'BlogContact'})