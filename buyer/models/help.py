from django.db import models

class Help(models.Model):
    phone_number = models.CharField(max_length=200,default='',blank=True,null=True)
    related_issue = models.CharField(max_length=200,default='',blank=True,null=True)
    message = models.CharField(max_length=1000,default='',blank=True,null=True)
