from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    phone=models.BigIntegerField(default=0)
    address=models.CharField(max_length=20,default="")
    is_superuser = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

