from django.db import models

# Create your models here.

class BlogContent(models.Model):
    header = models.CharField(max_length=500,default='',null=True,blank=True)
    content = models.CharField(max_length=100000,default='',null=True,blank=True)
    image = models.CharField(max_length=100000,default='',null=True,blank=True)
