from django.db import models
from companies_api.models import Company

class Contact(models.Model):
    # Create your models here.
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


