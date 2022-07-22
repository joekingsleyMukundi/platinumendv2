from django.urls import path
from . import views

urlpatterns = [
  path('dashboard/', views.get_dashboard, name='get_dashboard'),
  path('companies/', views.get_companies, name='get_companies'),
  path('company/<id>/', views.get_company, name='get_company'),
  path('transactions/', views.get_transactions, name='get_transactions'),
  path('profile/', views.get_profile, name='get_profile'),
  path('company/<id>/add_office', views.create_office, name='add_office'),
  path('office/<office_id>', views.office, name='edit_office'),
  path('edit_office/<office_id>', views.office, name='edit_office'),
  path('delete_office/<office_id>', views.office, name='delete_office'),
]