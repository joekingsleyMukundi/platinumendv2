from  django.db.models.signals import post_save
from .models import Client, Dashboard
from errors.custom_internal_server_error import InternalServerError
from message_queues.producer import publish

def  user_created(sender, instance, created, **kwargs):
    if created:
        user = instance
        try:
            client_dashboard = Dashboard.objects.create(client=user)
            publish('client_created', user)
        except Exception as e:
          print(e)
          raise InternalServerError();
post_save.connect(user_created, sender=Client)