import random
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.crypto import get_random_string
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class CustomUser(AbstractUser):
  id =  models.AutoField(primary_key=True)
  email = models.EmailField(verbose_name='Email', max_length=60, unique=True)
  username = models.CharField(verbose_name='Fullname', max_length=255)
  phone = models.CharField(max_length=255,null=True,blank=True)
  activationtoken = models.CharField (max_length= 255,default=get_random_string(length=32))
  role_status  =  models.CharField(max_length=255,default='completed')
  role = models.CharField(max_length=255,default='writer')
  is_verified = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  REQUIRED_FIELDS = ['username','phone']
  USERNAME_FIELD = 'email'
  
  def get_username(self):
      return self.email


class Company (models.Model):
  id =  models.AutoField(primary_key=True)
  owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  email = models.EmailField(verbose_name='Email', max_length=60, unique=True)
  phone = models.CharField(max_length=255,null=True,blank=True)

  def __str__(self):
      return self.name

# Create your models here.
