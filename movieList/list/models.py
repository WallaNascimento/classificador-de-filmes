from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
  # date = models.DateField
  
    def __str__(self):
        return self.name