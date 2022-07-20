from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decorators.auth_decorators import authenticate_user
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
@authenticate_user
def dashboard(request):
    user = request.user
    try:
        freelancer_data = Freelancer.objects.get(freelancer_id=user.id)
        serializer = FreelancerSerializer(freelancer_data, Many=False)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        raise DbException('Database error')