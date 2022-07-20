from rest_framework import serializers
from .models import *

class DashboardSerializer (serializers.ModelSerializer):
  class Meta:
    model = Dashboard
    fields = '__all__'

class WalletSeializer (serializers.ModelSerializer):
  class Meta:
    model = FreelancerWallet
    fields = '__all__'

class  FreelancerActivitySerializer (serializers.ModelSerializer):
  class Meta:
    model = FreelancerActivity
    fields = '__all__'

class FreelancerCurrentJobSerializer (serializers.ModelSerializer):
  class Meta:
    model = FreelancerCurrentJob
    fields = '__all__'

class FreelancerJobsDoneSerializer (serializers.ModelSerializer):
  class Meta:
    model = FreelancerJobsDone
    fields = '__all__'

class CheckinSerializer (serializers.ModelSerializer):
  class Meta:
    model = Checkin
    fields = '__all__'

class AttachmentsSerializer (serializers.ModelSerializer):
  class Meta:
    model = Attachments
    fields = '__all__'

class SkillsSerializer (serializers.ModelSerializer):
  class Meta:
    model = Skills
    fields = '__all__'

class FreelancerSerializer (serializers.ModelSerializer):
  class Meta:
    model = Freelancer
    fields = '__all__'
    def get_dashboard(self, obj):
      return DashboardSerializer(obj.dashboard).data
    def get_wallet(self, obj):
      return WalletSeializer(obj. freelancerWallet).data
    def get_activity(self, obj):
      activity = obj.FreelancerActivity_set.all()
      serializer = FreelancerActivitySerializer(activity, many=True)
      return serializer.data
    def get_current_job(self, obj):
      current_job = obj.FreelancerCurrentJob_set.all()
      serializer = FreelancerCurrentJobSerializer(current_job, many=True)
      return serializer.data
    def get_jobs_done(self, obj):
      jobs_done = obj.FreelancerJobsDone_set.all()
      serializer = FreelancerJobsDoneSerializer(jobs_done, many=True)
      return serializer.data
    def get_checkin(self, obj):
     return CheckinSerializer(obj.checkin).data
    def get_Attachments(self, obj):
      attachments = obj.Attachments_set.all()
      serializer = AttachmentsSerializer(attachments, many=True)
      return serializer.data
    def get_skills(self, obj):
      skills = obj.Skills_set.all()
      serializer = SkillsSerializer(skills, many=True)
      return serializer.data