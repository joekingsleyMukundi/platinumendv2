from rest_framework import serializers
from .models import *

class ClientDashboardSerializer(serializers.ModelSerializer):
  class Meta:
      model = Dashboard
      fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
  class Meta:
      model = Client
      fields = '__all__'

  def get_dashboard(self, obj):
    return ClientDashboardSerializer(obj.dashboard).data