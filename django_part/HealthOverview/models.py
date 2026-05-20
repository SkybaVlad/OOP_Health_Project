from django.db import models

from django.contrib.auth.models import AbstractUser
from django.forms.fields import CharField


class User(AbstractUser):
    name = CharField(max_length=120)
    surname = CharField(max_length=120)
    age = models.IntegerField()
    sex = CharField(max_length=5)
