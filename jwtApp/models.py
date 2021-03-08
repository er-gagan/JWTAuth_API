from django.db import models
from django.contrib.auth.models import AbstractUser

your_choices = (
        ('Super-Admin','Super-Admin'),
        ('Teacher','Teacher'),
        ('Student','Student'),
    )


class User(AbstractUser):
   Phone = models.CharField(max_length=15)
   Occupation = models.CharField(max_length=15, choices=your_choices)
