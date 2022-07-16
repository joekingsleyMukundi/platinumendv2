from django.db import models

# Create your models here.
class Users (models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.CharField(max_length=225)
    country = models.CharField(max_length=225)
    role = models.CharField(max_length=225)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
