from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    hour = models.IntegerField()
    minutes = models.IntegerField()
    slot = models.IntegerField()
