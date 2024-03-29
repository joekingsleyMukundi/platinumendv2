from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import  smart_str, force_str,  smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .models import *
from .errors import *
from .mails import *
from .producer import *

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email',
                  'username', 'phone', 'is_verified', 'is_active','role','role_status']

class ChangePasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length = 2)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        try:
            print(attrs.get('email'))
            email = attrs.get('email')
            if CustomUser.objects.filter(email=email).exists():
                user = CustomUser.objects.get(email=email)
                user.email
                uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
                token = PasswordResetTokenGenerator().make_token(user)
                url = 'http://127.0.0.1:3090/forgot-password/uid='+uidb64+'/token='+token+'/'
                subject = 'Password reset'
                message = 'You or someone else has initiated a password reset. if it was you click the link  to reset the password: '+url
                send_mail_to_user(user,subject,message)
                return user
            raise ValidationError('user doesnot exist')
        except Exception as e:
            print(e)
            raise CustomInternalServerError('Internal Server Error')

class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length = 5,write_only=True)
    confirm_password = serializers.CharField(min_length = 5,write_only=True)
    token = serializers.CharField(min_length=1,write_only=True)
    uidb64 = serializers.CharField(min_length=1,write_only=True)
    class Meta:
        fields=['password','confirm_password','token','uidb64']
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            confirm_password = attrs.get('confirm_password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')
            if password != confirm_password:
              raise RequestValidationError('password dont match')
            id = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise ValidationError('reset link is invalid')
            user.set_password(password)
            user.save()
            subject = 'Password reset success'
            message = 'Your password has succcesfully been reset'
            send_custom_email(subject,message,user.email)
            return user;
        except Exception as e:
            print(e)
            raise CustomInternalServerError('Internal server error')

class ActivateEmployerSerializer(serializers.Serializer):
    id= serializers.IntegerField(write_only=True)
    email = serializers.EmailField(write_only=True)

    class Meta:
        fields = ['id','email']
    def validate(self, attrs):
        try:
            id = attrs.get('id')
            email = attrs.get('email')
            if CustomUser.objects.filter(id=id).exists():
                user = CustomUser.objects.get(id=id)
                if user.email != email:
                    raise ValidationError('email dont match')
                user.role = 'employer'
                user.save()
                subject = 'Role activation'
                message = 'Welcome partner, your role has been activated. We are glad to add you to our esteemed employers'
                send_custom_email(subject,message,user.email)
                publish('employer_activated',user)
                return user
            raise ValidationError('user doesnot exist')
        except Exception as e:
            print(e)
            raise CustomInternalServerError('Internal Server Error')



class RegisterCompanySerializer (serializers.Serializer):
    id = serializers.IntegerField(write_only=True)
    name = serializers.CharField(min_length = 200,write_only=True)
    email = serializers.EmailField(write_only=True)
    phone = serializers.CharField(min_length = 10,write_only=True)
    class Meta:
        fields = ['name','email','phone','id']
    def validate(self, attrs):
        try:
            name = attrs.get('name')
            email = attrs.get('email')
            phone = attrs.get('phone')
            if CustomUser.objects.filter(id=id).exists():
                user = CustomUser.objects.get(id=id)
                if user.email != email:
                    raise ValidationError('email dont match')
                if Company.objects.filter(name=name).exists():
                    raise ValidationError('company name already exists')
                company = Company.objects.create(name=name, email=email, phone=phone, owner=user)
                subject = 'Company Set'
                message = 'Welcome , your company has been set. We are glad to add you to our esteemed Partners'
                send_custom_email(subject,message,user.email)
                print (company)
                publish('company_set',company)
                return Company
            raise ValidationError('user already exists')
        except Exception as e:
            print(e)
            raise CustomInternalServerError('Internal Server Error')

class BecomeClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(write_only=True)
    email = serializers.EmailField(write_only=True)
    class Meta:
        fields = ['id','email']
    def validate(self, attrs):
        try:
            id = attrs.get('id')
            email = attrs.get('email')
            if CustomUser.objects.filter(id=id).exists():
                user = CustomUser.objects.get(id=id)
                if user.email != email:
                    raise ValidationError('email dont match')
                user.role = 'client'
                user.save()
                subject = 'Role activation'
                message = 'Welcome partner, your role has been activated. We are glad to add you to our esteemed clients'
                send_custom_email(subject,message,user.email)
                publish('client_activated',user)
                return user
            raise ValidationError('user doesnot exist')
        except Exception as e:
            print(e)
            raise CustomInternalServerError('Internal Server Error')

class UpdateDetailsSerializer(serializers.Serializer):
    id = serializers.IntegerField(write_only=True)
    name = serializers.CharField(min_length = 200,write_only=True)
    email = serializers.EmailField(write_only=True)
    phone = serializers.CharField(min_length = 10,write_only=True)
    class Meta:
        fields = ['name','email','phone','id']
    def validate(self, attrs):
        try:
            id = attrs.get('id')
            name = attrs.get('name')
            email = attrs.get('email')
            phone = attrs.get('phone')
            if CustomUser.objects.filter(id=id).exists():
                user = CustomUser.objects.get(id=id)
                user.name = name
                user.email = email
                user.phone = phone
                user.save()
                return user
            raise ValidationError('user doesnot exist')
        except Exception as e:
            print(e)
            raise CustomInternalServerError('Internal Server Error')