
from django.db import models

# Create your models here.
# Table for device details (status : completed , Two atributes have to add after making user panel and adding employee table)
class DeviceRegistry(models.Model):
    Id = models.CharField( max_length=17,primary_key=True ,unique=True)
    DeviceType = models.CharField(max_length=20)
    DeviceVersion = models.CharField(max_length=20)
    DeviceLocation = models.CharField(max_length=50)
    PrimaryGroup = models.CharField(max_length=50)  # we want this field as nullable can be null  , NotRequired=True
    SecondaryGroup = models.CharField(max_length=50)  # we want this field as nullable can be null  , NotRequired=True
    Status = models.CharField(max_length=4 ,null=True)
    RegistrationTime = models.CharField(max_length=50)
    LastContact = models.TimeField(auto_now=False,auto_now_add=False, null=True) # we have to shift this attribute in DeviceLastUpdate Table
    # CreatedBy and LastEdited  ,these two attribute have to add after making user panel and adding employee table

    def __str__(self):
      return self.DeviceType

# # Table for ID , Last Conatact status 
# class DeviceLastUpdate(models.Model):
#     Id =  models.ForeignKey(DeviceRegistry, on_delete=models.DO_NOTHING)
#     LastContact = models.TimeField(auto_now=False,auto_now_add=False, null=True)
#     Status = models.CharField(max_length=4 ,null=True)
    
    # def __str__(self):
    #   return self.Id
