from django.db import models
from django.contrib.postgres.fields import ArrayField
from freelancer.models import Freelancer

# Create your models here.

class Client(models.Model):
    client_id = models.IntegerField()
    name = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.CharField(max_length=225)
    country = models.CharField(max_length=225)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Dashboard (models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    jobs_posted = models.IntegerField(default=0)
    amount_paid = models.IntegerField(default=0)
    completed_jobs = models.IntegerField(default=0)
    pending_jobs = models.IntegerField(default=0)
    account_balance = models.IntegerField(default=0)

    def __str__(self):
      return self.client.name
    