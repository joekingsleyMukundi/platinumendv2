from django.urls import path
from . import views

urlpatterns = [
  path('dashboard/', views.get_dashboard, name='get_dashboard'),
  path('company/', views.get_company, name='get_company'),
  path('transactions/', views.get_transactions, name='get_transactions'),
  path('profile/', views.get_profile, name='get_profile'),
]