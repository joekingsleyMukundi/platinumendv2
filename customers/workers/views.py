from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decorators.auth_decorators import authenticate_user
from .models import *
from .serializers import *

# Create your views here.

def dashboard (request):
    user = request.user
    try:
        worker_data = Worker.objects.get(worker_id=user.id)
        serializer = WorkerSerializer(worker_data, Many=False)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        raise DbException('Database error')