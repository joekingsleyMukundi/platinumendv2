from django.urls import path
from . import views

urlpatterns = [
  path('dashboard/', views.dashboard, name='dashboard'),
  path('users/',views.list_users, name='list_users'),
]