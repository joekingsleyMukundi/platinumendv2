from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Freelancer(models.Model):
    freelancer_id = models.IntegerField()
    name = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.CharField(max_length=225)
    country = models.CharField(max_length=225)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Dashboard(models.Model):
  freelancer = models.OneToOneField(Freelancer, on_delete=models.CASCADE)
  name = models.CharField(max_length=225)
  descriptiion = models.TextField()
  email = models.EmailField()
  phone = models.CharField(max_length=225)
  rating = models.IntegerField(default=0)
  country = models.CharField(max_length=225)
  is_verified = models.BooleanField(default=False)
  about = models.TextField()
  has_worked = models.BooleanField(default=False)
  hourly_rate = models.IntegerField(default=0)
  jobs_done = models.IntegerField(default=0)
  rehired_times = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name

class Skills (models.Model):
  freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
  skill = models.CharField(max_length=225)
  def __str__(self):
    return self.skill

class Attachments(models.Model):
  freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
  attachment = models.FileField(upload_to='attachments/')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.attachment.name

class FreelancerWallet(models.Model):
  freelancer = models.OneToOneField(Freelancer, on_delete=models.CASCADE)
  amount = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.freelancer.name

class FreelancerActivity(models.Model):
  freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
  activity = models.CharField(max_length=225)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.freelancer.name


class FreelancerCurrentJob(models.Model):
  freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
  title = models.CharField(max_length=225)
  amount_payable = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=225)

  def __str__(self):
    return self.freelancer.name

class FreelancerJobsDone(models.Model):
  freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
  title = models.CharField(max_length=225)
  amount_payable = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=225)

  def __str__(self):
    return self.freelancer.name

class Checkin(models.Model):
  freelancer = models.OneToOneField(Freelancer, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=225)


  def __str__(self):
    return self.freelancer.name
