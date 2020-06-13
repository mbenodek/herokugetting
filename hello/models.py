from django.db import models

# Create your models here.


class PersonalInfo(models.Model):
    name = models.CharField(max_length=256)
    designation = models.CharField(max_length=256)
