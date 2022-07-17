from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
  path('', include('djoser.urls')),
  path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('activate/<str:uid>/<str:token>/',views.activate, name='activate_users'),
  path('password_reset_request/',views.reset_password_request, name='password_reset_request'),
  path('password_reset/<str:uidb64>/<str:token>/',views.reset_password, name='password_reset'),
  path('set_new_password/',views.set_new_password, name='set_new_password'),
  path('request/become_employer/',views.become_employer_request, name='become_employer_request'),
  path('activate/employer/', views.activate_employer, name='activate_employer'),
  path('register_company/',views.register_company, name='register_company'),
  path('set_company/',views.set_company, name='set_company'),
  path('become_client/',views.become_client, name='become_client'),
]
