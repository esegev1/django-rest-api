from django.db import models

class Contact(models.Model):
    # Create your models here.
    name = models.CharField(max_length=32)
    age = models.IntegerField()


