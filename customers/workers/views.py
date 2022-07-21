from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decorators.auth_decorators import authenticate_user
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
@authenticate_user
def dashboard (request):
    user = request.user
    try:
        worker_data = Worker.objects.get(worker_id=user.id)
        serializer = WorkerSerializer(worker_data, Many=False)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        raise DbException('Database error')

@api_view(['GET'])
@authenticate_user
def join_company(request, id, office_id):
    user = request.user
    try:
        worker = Worker.objects.get(worker_id=user.id)
        company = Company.objects.get(id=id)
        office = Office.objects.get(id=office_id)
        worker.office = office
        worker.save()
        serializer = WorkerSerializer(worker, Many=False)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        raise DbException('Database error')