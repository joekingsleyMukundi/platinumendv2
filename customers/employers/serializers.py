from rest_framework import serializers
from .models import *

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'

class DashboardSerializer(serializers.ModelSerializer):
  class Meta:
      model = Dashboard
      fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
  class Meta:
      model = Company
      fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
  class Meta:
      model = Transaction
      fields = '__all__'