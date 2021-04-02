from django.shortcuts import render
from django.http import HttpResponse
from .models import post, Threads
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
def home(request):
	context={
	'dicpost': post.objects.all(),
	}
	return render(request, 'blog/bloghome.html', context)

class postListView(ListView):
	model = post
	template_name = 'blog/bloghome.html'
	context_object_name = 'dicpost'
	ordering = ['-datePosted']

class postDetailView(DetailView):
	model = post

class postCreateView(LoginRequiredMixin, CreateView):
	model = post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class postUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
	model = post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False

class postDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

	model = post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False

def about(request):
	return render(request, 'blog/blogabout.html', {'title':'BlogAbout'})

def contact(request):
	return render(request, "blog/blogcontact.html", {'title': 'BlogContact'})
