from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    group = models.CharField(max_length=10)