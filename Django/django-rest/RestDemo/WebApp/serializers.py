
from rest_framework import serializers
from rest_framework.serializers import Serializer
from .models import Student
from WebApp.models import Employee



class EmployeeSerializer(serializers.Serializer):

    EmpId = serializers.IntegerField()
    FirstName =  serializers.CharField(max_length=50)
    LastName  =  serializers.CharField(max_length=50)
    # fields = '__all__'


class StudentSerializer(serializers.Serializer):
    RollNo = serializers.IntegerField() 
    Name   = serializers.CharField(max_length=100) 
    City   = serializers.CharField(max_length=50) 

    # for inserting data in table through api
    # Creating Data
    def create(self, validated_data):       
        return Student.objects.create(**validated_data)     