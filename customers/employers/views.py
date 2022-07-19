from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import status
from decorators.auth_decorator import 
from .models import Dashboard
from .serializers import DashboardSerializer
from errors.custom_internal_server_error import InternalServerError

# Create your views here.
@api_view(['GET'])
@authenticate_user
def get_dashboard (request):
  user = request.user
  try:
      employer = Employer.objects.get(employer_id = user['id'])
      employer_dashboard_data = Dashboard.objects.get(employer = employer)
      serializer = DashboardSerializer(employer_dashboard_data, many=False)
      return Response(serializer.data, status=status.HTTP_200_OK)
  except Exception as e:
    raise InternalServerError();

@api_view(['GET'])
@authenticate_user
def get_company(request):
  user = request.user
  try:
      employer = Employer.objects.get(employer_id = user['id'])
      serializer = CompanySerializer(employer.company, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
  except Exception as e:
    raise InternalServerError();

@api_view(['GET'])
@authenticate_user
def get_transactions(request):
  user = request.user
  try:
      employer = Employer.objects.get(employer_id = user['id'])
      serializer = TransactionSerializer(employer.transactions, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
  except Exception as e:
    raise InternalServerError();