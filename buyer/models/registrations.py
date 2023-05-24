from django.db import models

# Create your models here.
class User(models.Model):
    phone_number = models.CharField(max_length=200,default='',blank=True,null=True)
    name = models.CharField(max_length=200,default='',blank=True,null=True)
    email_id = models.CharField(max_length=200,default='',blank=True,null=True)
    gender = models.CharField(max_length=200,default='',blank=True,null=True)
    address = models.CharField(max_length=200,default='',blank=True,null=True)
    pincode = models.CharField(max_length=200,default='',blank=True,null=True)
    city = models.CharField(max_length=200,default='',blank=True,null=True)
    state = models.CharField(max_length=200,default='',blank=True,null=True)

class OTP(models.Model):
    phone_number = models.CharField(max_length=200,default='',blank=True,null=True)
    otp = models.CharField(max_length=200,default='',blank=True,null=True)