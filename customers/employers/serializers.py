from rest_framework import serializers
from .models import *

class DashboardSerializer(serializers.ModelSerializer):
  class Meta:
      model = Dashboard
      fields = '__all__'

class OfficeSerializer(serializers.ModelSerializer):
  class Meta:
      model = Office
      fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
      model = Company
      fields = '__all__'

    def get_office(self, obj):
        office = obj.Office_set.all()
        serializer = OfficeSerializer(office, many=True)
        return serializer.data

class TransactionSerializer(serializers.ModelSerializer):
  class Meta:
      model = Transactions
      fields = '__all__'

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'
    
    def get_dashboard(self, obj):
        return DashboardSerializer(obj.dashboard).data
    def get_company(self, obj):
        company = obj.Company_set.all()
        serializer = CompanySerializer(company, many=True)
        return serializer.data
    def get_transactions(self, obj):
        transactions = obj.Transaction_set.all()
        serializer = TransactionSerializer(transactions, many=True)
        return serializer.data