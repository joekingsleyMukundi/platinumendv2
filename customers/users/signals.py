from  django.db.models.signals import post_save
from .models import Users
from  freelancer.models import Freelancer
from errors.custom_internal_server_error import InternalServerError

def  user_created(sender, instance, created, **kwargs):
    if created:
        user = instance
        try:
            freelancer = Freelancer.objects.create(freelancer_id=user.id, name=user.name, email=user.email, phone=user.phone, is_verified=user.is_verified)
        except Exception as e:
          print(e)
          raise InternalServerError();
post_save.connect(user_created, sender=Users)