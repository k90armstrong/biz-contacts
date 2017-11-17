from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, blank=True)
    business_name = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    cell_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    work_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    email_regex = RegexValidator(regex=r'\w+@\w+\.\w+$')
    email = model.CharField(validators=[email_regex], max_length=200, blank=True) 
    notes = models.CharField(max_length=500, blank=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)


class Image(models.Model):
    front_url =  models.CharField(max_length=300, blank=True)
    back_url =  models.CharField(max_length=300, blank=True)

class Address(models.model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=300, blank=True)
    address2 = models.CharField(max_length=300, blank=True)
    city = models.CharField(max_length=300, blank=True)
    state = models.CharField(max_length=300, blank=True)
    country = models.CharField(max_length=300, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    
    
    

    
