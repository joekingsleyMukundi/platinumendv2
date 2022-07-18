from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from .models import CustomUser
from .decorators import *
from .errors import *
from .producers import *

# Create your views here.

# creting a custom jwt generator class to add more items to the token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims in our case adding the username
        token['username'] = user.username
        token['is_active']= user.is_active
        token['email'] = user.email
        token['role'] = user.role
        # ...

        return token
# creating a class based view for the jwt url inheriting the token generator class above
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Create your views here.

@api_view(['GET'])
@user_not_active
def activate (request, uid, token):
    try:
        id = smart_str(urlsafe_base64_decode(uid))
    except Exception as e:
        print(e)
        raise CustomInternalServerError(e)
    # check wheather the user exists
    if not CustomUser.objects.filter(id = id).exists():
        raise ValidationError('user does not exist')
    user = CustomUser.objects.get(id = id)
    user_token= user.activationtoken
    if token != user_token:
        raise ValidationError('invalid token')
    user.is_active = True
    try:
        user.save()
        # publishing the message to the queue
        publish('user_created', user)
    except Exception as e:
        print(e)
        raise CustomInternalServerError(e)
    print('success')
    serializer = UserSerialiser(user, many=False)
    return Response(serializer.data)

@api_view(['GET','POST'])
def reset_password_request(request):
  if request.method == 'POST':
    serializer = ChangePasswordRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception = True);
    return Response ('success')
  return Response('reset password')


@api_view(['GET'])
def reset_password(request, uidb64, token):
  try:
      id = smart_str(urlsafe_base64_decode(uidb64))
      user = CustomUser.objects.get(id=id)
      if not PasswordResetTokenGenerator().check_token(user,token):
          raise ValidationError('invalid reset token')
      return Response({'success':True,'message':'Credentials are valid','uidb64':uidb64,'token':token})
  except Exception as e:
      raise CustomInternalServerError('Internal serevr error')

@api_view(['PATCH'])
def set_new_password(request):
  serializer = ChangePasswordSerializer(data=request.data)
  serializer.is_valid(raise_exception = True)
  return Response({'success':True,'message':'Password reset  successfully'},status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def set_company (request):
  serializer = SetCompanySerializer(data=request.data)
  serializer.is_valid(raise_exception = True)
  return Response({'success':True,'message':'Company set successfully'},status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def register_company (request):
  serializer = RegisterCompanySerializer(data=request.data)
  serializer.is_valid(raise_exception = True)
  return Response({'success':True,'message':'Company set successfully'},status=status.HTTP_200_OK)

@api_view(['PATCH'])
@permission_classes((IsAuthenticated, ))
def become_employer_request(request):
    serializer = BecomeEmployerRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception = True);
    return Response ('success')

@api_view(['PATCH'])
@permission_classes((IsAuthenticated, ))
def activate_employer(request):
    serializer = ActivateEmployerSerializer(data=request.data)
    serializer.is_valid(raise_exception = True);
    return Response ('success')

@api_view(['PATCH'])
@permission_classes((IsAuthenticated, ))
def become_client(request):
    serializer = BecomeClientSerializer(data=request.data)
    serializer.is_valid(raise_exception = True);
    return Response ('success')