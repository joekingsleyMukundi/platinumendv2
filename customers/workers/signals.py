from  django.db.models.signals import post_save
from .models import Worker, Dashboard
from errors.custom_internal_server_error import InternalServerError
from message_queue.producer import publish

def  user_created(sender, instance, created, **kwargs):
    if created:
        user = instance
        try:
            worker_dashboard = Dashboard.objects.create(worker=user)
            publish('worker_created', user)
        except Exception as e:
          print(e)
          raise InternalServerError();
post_save.connect(user_created, sender=Worker)
