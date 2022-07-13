from django.urls import path
from . import views

urlpatterns =[
  path('employer/dashboard/', views.dashboard, name='dashboard'),
  path('employer/dashboard/profile/', views.profile, name='profile'),
  path('employer/dashboard/profile/edit/', views.edit_profile, name='edit_profile'),
]