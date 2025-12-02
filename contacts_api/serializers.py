from rest_framework import serializers
from .models import Contact
from companies_api.serializers import CompanySerializer

class ContactSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model=Contact
        fields=('id','name','age', 'company')
        