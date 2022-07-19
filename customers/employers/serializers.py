from rest_framework import serializers
from .models import *
 class DashboardSerializer(serializers.ModelSerializer):
   class Meta:
       model = Dashboard
       fields = '__all__'