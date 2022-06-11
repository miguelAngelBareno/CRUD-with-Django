from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
class Business(models.Model):
    company_name = models.CharField(max_length=50)
    direction = models.CharField(max_length=20)
    NIT = models.CharField(unique=True, max_length=10) #includes verification digit
    phone = PhoneNumberField()  #cell phone or landline
