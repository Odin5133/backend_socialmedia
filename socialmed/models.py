from django.db import models

# Create your models here.

class loginInfo(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=18)
