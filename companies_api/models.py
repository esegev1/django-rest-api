from django.db import models

class Company(models.Model):
    # Create your models here.
    name = models.CharField(max_length=100)
    industry = models.CharField(max_length=50)

