from django.db import models

# Create your models here.
class Employer (models.Model):
  username = models.CharField(max_length=200)
  email = models.EmailField()
  phone = models.CharField(max_length=200)
  is_active = models.BooleanField(default=True)

class Dashboard (models.Model):
  employer = models.OneToOneField(Employer, on_delete=models.CASCADE)
  all_workers = models.IntegerField(default=0)
  all_pending_jobs = models.IntegerField(default=0)
  all_approved_jobs = models.IntegerField(default=0)
  all_completed_jobs = models.IntegerField(default=0)
  all_completed_payment = models.IntegerField(default=0)
  live_worker_payment = models.IntegerField(default=0)
  pending_payment = models.IntegerField(default=0)
  checked_in_workers = models.IntegerField(default=0)
  is_verified = models.BooleanField(default=False)
  def __str__(self):
    return self.username