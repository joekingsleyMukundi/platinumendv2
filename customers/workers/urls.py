from django.urls import path
from . import views


urlpatterns = [
  path('worker/dashboard/', views.dashboard, name='dashboard'),
]