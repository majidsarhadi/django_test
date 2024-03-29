from django.db import models
# Create your models here.

class Student(models.Model):
    full_name=models.CharField(max_length=30,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    address=models.CharField(max_length=50,null=True,blank=True)
    nation_id=models.CharField(max_length=10)
    phone=models.CharField(max_length=11,null=True,blank=True)
    user_name=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
