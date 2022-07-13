from django.db import models
from employers.models import Employer
from workers.models import Worker

class Company (models.Model):
  name = models.CharField(max_length=255)
  owner = models.ForeignKey(Employer, on_delete=models.CASCADE)
  workers = ArrayField(models.ForeignKey(Worker, on_delete=models.CASCADE))
  email = models.EmailField(verbose_name='Email', max_length=60, unique=True)
  phone = models.CharField(max_length=255,null=True,blank=True)

  def __str__(self):
    return self.name