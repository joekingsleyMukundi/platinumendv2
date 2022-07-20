from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from decorators.auth_decorators import authenticate_user
from .models import *
from .serializers import *
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

@api_view(['GET'])
@authenticate_user
def get_profile(request):
  user = request.user
  try:
      employer = Employer.objects.get(employer_id = user['id'])
      serializer = EmployerSerializer(employer, many=False)
      return Response(serializer.data, status=status.HTTP_200_OK)
  except Exception as e:
    raise InternalServerError();