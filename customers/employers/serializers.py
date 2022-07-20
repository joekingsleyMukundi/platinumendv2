from rest_framework import serializers
from .models import *

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

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'
    
    def get_dashboard(self, obj):
        return DashboardSerializer(obj.dashboard).data
    def get_company(self, obj):
        return CompanySerializer(obj.company).data
    def get_transactions(self, obj):
        return TransactionSerializer(obj.transactions).data