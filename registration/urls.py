
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.SuccessPage, name='success'),
    path('register/', views.RegisterUser, name='register'),
]