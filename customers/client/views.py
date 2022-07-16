from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decorators.auth_decorators import authenticate_user
from .models import *
# Create your views here.
@api_view(['GET'])
@authenticate_user
def client_dashboard(request):
    client = request.user
    try:
        client_data = Client.objects.get(client_id=client.id)
        dashboard_data = Dashboard.objects.get(client=client_data)
        serializer = DashboardSerializer(dashboard_data, Many=False)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        raise DbException('Database error')

@api_view (['GET'])
@authenticate_user
def client_profile(request):
    client = request.user
    try:
        client_data = Client.objects.get(client_id=client.id)
        serializer = ClientSerializer(client_data, Many=False)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        raise DbException('Database error')
