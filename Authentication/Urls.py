from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('manage_users/', views.manage_users, name='manage_users'),
]
