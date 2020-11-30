from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   Phone = models.CharField(max_length=15)
   Occupation = models.CharField(max_length=15)