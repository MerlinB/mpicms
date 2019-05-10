from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.IntegerField(null=True, blank=True)
    office = models.CharField(max_length=31, blank=True)
