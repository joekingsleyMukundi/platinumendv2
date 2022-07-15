from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
  path('auth/', include('djoser.urls')),
  path('auth/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('auth/activate/<str:uid>/<str:token>/',views.activate, name='activate_users'),
  path('auth/password_reset_request/',views.reset_password_request, name='password_reset_request'),
  path('auth/password_reset/<str:uidb64>/<str:token>/',views.reset_password, name='password_reset'),
  path('auth/set_new_password/',views.set_new_password, name='set_new_password'),
  path('auth/request/become_employer/',views.become_employer_request, name='become_employer_request'),
  path('auth/activate/employer/', views.activate_employer, name='activate_employer'),
  path('auth/register_company/',view.register_company, name='register_company'),
  path('auth/set_company/',views.set_company, name='set_company'),
  path('auth/become_client/',views.become_client, name='become_client'),
]
