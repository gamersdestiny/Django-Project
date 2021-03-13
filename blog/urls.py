
from django.urls import path, include
from .import views 


urlpatterns = [
    path('' , views.home, name='Blog_Home'),
    path('about/', views.about, name='Blog_About'),
    path('contact/', views.contact, name='Contact')
]