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
def get_companies(request):
  user = request.user
  try:
      employer = Employer.objects.get(employer_id = user['id'])
      serializer = CompanySerializer(employer.company, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
  except Exception as e:
    raise InternalServerError();
@api_view(['GET', 'PATCH'])
@authenticate_user
def get_company(request, id):
  user = request.user
  try:
      employer = Employer.objects.get(employer_id = user['id'])
      company = Company.objects.get(id = id)
      if request.method == 'GET':
        serializer = CompanySerializer(company, many=False)
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

@api_view(['POST'])
@authenticate_user
def create_office(request, id):
  user = request.user
  try:
    office_ctegory = request.data['office_category']
    company = Company.objects.get(id = id)
    office = Office.objects.create(company = company,office_category=office_category);
    serializer = OfficeSerializer(office, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  except Exception as e:
    print(e)
    raise InternalServerError();

@api_view(['GET','PATCH','DELETE'])
@authenticate_user
def office(request, office_id):
  user = request.user
  try:
    office = Office.objects.get(id = office_id)
    serializer=OfficeSerializer(office, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)
  except Exception as e:
    print(e)
    raise InternalServerError();
  if request.method == 'PATCH':
    try:
      office_category = request.data['office_category']
      office.office_category = office_category
      office.save()
      serializer = OfficeSerializer(office, many=False)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
      print(e)
      raise InternalServerError();
  if request.method == 'DELETE':
    try:
      office.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
      print(e)
      raise InternalServerError();
