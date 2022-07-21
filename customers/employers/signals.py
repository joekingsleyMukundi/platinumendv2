from  django.db.models.signals import post_save
from .models import Employer, Dashboard
from errors.custom_internal_server_error import InternalServerError

def  user_created(sender, instance, created, **kwargs):
    if created:
        user = instance
        try:
            employer_dashboard = Dashboard.objects.create(employer=user)
        except Exception as e:
          print(e)
          raise InternalServerError();
post_save.connect(user_created, sender=Employer)
