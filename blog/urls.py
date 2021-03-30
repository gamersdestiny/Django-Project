
from django.urls import path, include
from .import views 
from blog.views import postListView, postDetailView, postCreateView

urlpatterns = [
    path('' , postListView.as_view(), name='Blog_Home'),
    path('post/<int:pk>' , postDetailView.as_view(), name='postDetail'),
    path('post/create/', postCreateView.as_view(), name='postCreate'),
    path('about/', views.about, name='Blog_About'),
    path('contact/', views.contact, name='Contact'),
]	