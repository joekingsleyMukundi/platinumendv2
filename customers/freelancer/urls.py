from django.urls import path
from . import views

urlpatterns = [
  path('freelancer/dashboard/', views.dashboard, name='dashboard'),
]