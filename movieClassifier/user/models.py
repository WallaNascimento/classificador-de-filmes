from django.db import models

from django.contrib.auth.models import AbstractUser, Permission, Group

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    
    def __str__(self) -> str:
        return self.name
