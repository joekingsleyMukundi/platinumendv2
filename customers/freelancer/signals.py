from  django.db.models.signals import post_save
from .models import Freelancer
from  freelancer.models import Freelancer
from errors.custom_internal_server_error import InternalServerError

def  user_created(sender, instance, created, **kwargs):
    if created:
        user = instance
        try:
            freelancer_dashboard = Dashboard.objects.create(freelancer=user)
        except Exception as e:
          print(e)
          raise InternalServerError();
post_save.connect(user_created, sender=Freelancer)