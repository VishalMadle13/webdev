from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import IntegerField

# Create your models here.


class Employee(models.Model):
    EmpId = models.IntegerField()
    FirstName =  models.CharField(max_length=50)
    LastName  =  models.CharField(max_length=50)
    def __str__(self):
        return self.FirstName

class Student(models.Model):
    RollNo = models.IntegerField() 
    Name   = models.CharField(max_length=100) 
    City   = models.CharField(max_length=50)      