from django.db import models

# Create your models here.


class Enquiry(models.Model):
    name = models.CharField(max_length=50) 
    address = models.CharField(max_length=150) 
    age = models.CharField(max_length=10) 
    gender = models.CharField(max_length=10) 
    email = models.CharField(max_length=50) 
    contact = models.CharField(max_length=10) 


def __str__(self):
    return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=50) 
    price = models.CharField(max_length=15) 
    unit = models.CharField(max_length=10) 
    date = models.CharField(max_length=20) 
    description = models.CharField(max_length=50) 
     


def __str__(self):
    return self.name

class Plan(models.Model):
    name = models.CharField(max_length=50) 
    amount = models.CharField(max_length=15) 
    duration = models.CharField(max_length=10) 
     


def __str__(self):
    return self.name


class Member(models.Model):
    name = models.CharField(max_length=50) 
    contact = models.CharField(max_length=10) 
    emailid = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    plan = models.CharField(max_length=10)
    join_date = models.CharField(max_length=40) 
    expiry_date = models.CharField(max_length=40)  
    intial_amount = models.CharField(max_length=50)  
     


def __str__(self):
    return self.name
    