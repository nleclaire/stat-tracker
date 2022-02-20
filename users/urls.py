"""Defines url patterns for users."""

from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    # Login page
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Logout page
    path('users/', views.logout_view, name='logout'),
    # Registration form
    path('register', views.register, name='register')
]
