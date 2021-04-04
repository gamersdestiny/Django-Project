
from django.urls import path, include
from .import views 
from blog.views import postListView, postDetailView, postCreateView, postUpdateView, postDeleteView, userPostListView, userProfileListView

urlpatterns = [
    path('' , postListView.as_view(), name='Blog_Home'),
    path('user/<str:username>' , userPostListView.as_view(), name='userPosts'),
    path('user/profile/<str:username>' , userProfileListView.as_view(), name='userProfile'),
    path('post/<int:pk>' , postDetailView.as_view(), name='postDetail'),
    path('post/create/', postCreateView.as_view(), name='postCreate'),
    path('post/<int:pk>/update', postUpdateView.as_view(), name='postUpdate'),
    path('post/<int:pk>/delete', postDeleteView.as_view(), name='postDelete'),
    path('about/', views.about, name='Blog_About'),
    path('contact/', views.contact, name='Contact'),
]	