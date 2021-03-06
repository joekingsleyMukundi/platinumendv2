from django.db import models
from employers.models import Office
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Worker (models.Model):
  worker_id = models.IntegerField()
  username = models.CharField(max_length=200)
  email = models.EmailField()
  phone = models.CharField(max_length=200)
  def __str__(self):
    return self.username

class Dashboard (models.Model):
  worker = models.OneToOneField(Worker, on_delete=models.CASCADE)
  all_pending_jobs = models.IntegerField(default=0)
  all_approved_jobs = models.IntegerField(default=0)
  all_completed_jobs = models.IntegerField(default=0)
  all_completed_payment = models.IntegerField(default=0)
  live_worker_payment = models.IntegerField(default=0)
  pending_payment = models.IntegerField(default=0)
  is_verified = models.BooleanField(default=False)
  def __str__(self):
    return self.username

class Activities(models.Model):
  worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
  activity = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.activity

class Jobs (models.Model):
  title = models.CharField(max_length=255)
  amount_payable = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=255)
  worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
  office = models.ForeignKey(Office, on_delete=models.CASCADE)

  def __str__(self):
    return self.title


