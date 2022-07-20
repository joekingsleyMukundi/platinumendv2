from rest_framework import serializers
from .models import *

class DashboardSerializer (serializers.ModelSerializer):
  class Meta:
    model = Dashboard
    fields = '__all__'

class ActivitiesSerializer (serializers.ModelSerializer):
  class Meta:
    model = Activities
    fields = '__all__'

class CurrentJobsSerializer (serializers.ModelSerializer):
  class Meta:
    model = Jobs
    fields = '__all__'

class workerSerializer (serializers.ModelSerializer):
  class Meta:
    model = Worker
    fields = '__all__'

    def get_dashboard(self, obj):
      return DashboardSerializer(obj.dashboard).data
    def get_activities(self, obj):
      activity = obj.Activities_set.all()
      serializer = ActivitiesSerializer(activity, many=True)
      return serializer.data
    def get_current_job(self, obj):
      current_job = obj.Jobs_set.all()
      serializer = CurrentJobsSerializer(current_job, many=True)
      return serializer.data