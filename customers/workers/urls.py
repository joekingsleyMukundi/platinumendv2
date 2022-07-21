from django.urls import path
from . import views


urlpatterns = [
  path('dashboard/', views.dashboard, name='dashboard'),
  path('join/company/<id>/office/<office_id>', views.join_company, name='join_company'),
]