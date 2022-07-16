from django.urls import path
from . import views

urlpatterns=[
  path('',views.client_dashboard,name='client_dashboard'),
  path('profile/',views.client_profile,name='client_profile'),
]