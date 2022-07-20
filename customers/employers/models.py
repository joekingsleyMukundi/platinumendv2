from django.db import models
import workers.models as workers
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Employer (models.Model):
  employer_id = models.IntegerField()
  username = models.CharField(max_length=200)
  email = models.EmailField()
  phone = models.CharField(max_length=200)
  is_verified = models.BooleanField(default=False)

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
  salaries_current = models.IntegerField(default=0)
  salaries_previous = models.IntegerField(default=0)
  def __str__(self):
    return self.username



class Company (models.Model):
  company_id = models.IntegerField()
  owner = models.ForeignKey(Employer, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  email = models.EmailField(verbose_name='Email', max_length=60, unique=True)
  phone = models.CharField(max_length=255,null=True,blank=True)

  def __str__(self):
    return self.name

class Office (models.Model):
  company = models.ForeignKey(Company, on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  workers = models.ForeignKey('workers.Worker', on_delete=models.CASCADE)
  office_category =  models.CharField(max_length=255)
  owed_amount = models.IntegerField(default=0)
  paid_amount = models.IntegerField(default=0)
  def __str__(self):
    return self.name

class CheckedIn (models.Model):
  worker = models.ForeignKey('workers.Worker', on_delete=models.CASCADE)
  office = models.ForeignKey(Office, on_delete=models.CASCADE)
  is_checked_in = models.BooleanField(default=False)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)

class Transactions (models.Model):
  transaction_id = models.CharField(max_length=255)
  transaction_amount = models.IntegerField(default=0)
  transaction_type = models.CharField(max_length=255)
  receiver = models.ForeignKey('workers.Worker', on_delete=models.CASCADE)
  sender = models.ForeignKey(Employer, on_delete=models.CASCADE)
  created_at = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.transaction_id