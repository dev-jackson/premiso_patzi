import datetime

from django.db import models
from django.db import timezone
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }
