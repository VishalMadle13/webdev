from dataclasses import dataclass
from datetime import datetime
from time import timezone
from urllib.request import Request
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from DeviceRegistrar.models import DeviceRegistry

from django.db import connection
import datetime
# Create your views here.
def DeviceRegistar(request):
    return render(request,"DeviceRegistrar.html")

def ShowData(request):
    data = DeviceRegistry.objects.all()
    # Below commented code is for joining two tables 
    # cursor = connection.cursor()
    # cursor.execute("select DeviceRegistry.Id,DeviceRegistry.DeviceType,DeviceRegistry.DeviceLocation,DeviceRegistry.PrimaryGroup,DeviceRegistry.SecondaryGroup,DeviceLastUpdate.LastContact,DeviceLastUpdate.Status from DeviceRegistry join DeviceLastUpdate on DeviceRegistry.Id=DeviceLastUpdate.Id")
    # result = cursor.fetchall()
    return render(request,"ShowData.html",{'data':data})    



def send(request):
    if request.method=='POST':
        #taking the values or data entered by user in form by post method 
        Id = request.POST['Id']
        DeviceType = request.POST['DeviceType']
        DeviceVersion = request.POST['DeviceVersion']
        DeviceLocation = request.POST['DeviceLocation']
        PrimaryGroup = request.POST['PrimaryGroup']
        SecondaryGroup = request.POST['SecondaryGroup']
        now = datetime.datetime.now()
        
        #writing the data in database i.e. model whose name is DeviceRegistry 
        DeviceRegistry(Id =Id,DeviceType=DeviceType,DeviceLocation=DeviceLocation,PrimaryGroup=PrimaryGroup,SecondaryGroup=SecondaryGroup,DeviceVersion=DeviceVersion,RegistrationTime = now).save()

        msg = "Device registerd Successfully"
        
        print("time : ",now)
        return render(request,"DeviceRegistrar.html",{'msg':msg,'now':now})
        
    else:
        return HttpResponse("<h1> request is not post </h1>")


def delete(request):
    Id = request.GET['Id']
    DeviceRegistry.objects.filter(Id=Id).delete()
    print("delete was clicked")
    return HttpResponseRedirect("show/")

def edit(request):
    Id = request.GET['Id']  # getting the id of device that have to edit  
    PrimaryGroup = SecondaryGroup ="Not Available"
    for data in DeviceRegistry.objects.filter(Id=Id):
        Id  = data.Id
        DeviceType = data.DeviceType
        DeviceVersion = data.DeviceVersion
        DeviceLocation = data.DeviceLocation
        PrimaryGroup = data.PrimaryGroup
        SecondaryGroup = data.SecondaryGroup
     
    return render(request,"edit.html",{'Id':Id,'DeviceType':DeviceType,'DeviceVersion':DeviceVersion,'DeviceLocation':DeviceLocation,'PrimaryGroup':PrimaryGroup,'SecondaryGroup':SecondaryGroup})

def RecordEdited(request):
    if request.method =="POST":
        Id = request.POST['Id']
        DeviceType = request.POST['DeviceType']
        DeviceVersion = request.POST['DeviceVersion']
        DeviceLocation = request.POST['DeviceLocation']
        PrimaryGroup = request.POST['PrimaryGroup']
        SecondaryGroup = request.POST['SecondaryGroup']
        DeviceRegistry.objects.filter(Id=Id).update(Id=Id,DeviceType=DeviceType,DeviceVersion=DeviceVersion,DeviceLocation=DeviceLocation,PrimaryGroup=PrimaryGroup,SecondaryGroup=SecondaryGroup)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")

def more(request):
    Id = request.GET['Id']  # getting the id of device that have to show more details
    for data in DeviceRegistry.objects.filter(Id=Id):
        Id  = data.Id
        DeviceType = data.DeviceType
        DeviceVersion = data.DeviceVersion
        DeviceLocation = data.DeviceLocation
        PrimaryGroup = data.PrimaryGroup
        SecondaryGroup = data.SecondaryGroup
        RegistrationTime = data.RegistrationTime
        Status = data.Status
        LastContact = data.LastContact   # LastConntact :we have to shift this attribute in DeviceLastUpdate and can access by foreign key
        
    return render(request,"MoreDetails.html",{'Id':Id,'DeviceType':DeviceType,'DeviceVersion':DeviceVersion,'DeviceLocation':DeviceLocation,'PrimaryGroup':PrimaryGroup,'SecondaryGroup':SecondaryGroup,'LastContact':LastContact,'RegistrationTime':RegistrationTime,'Status':Status})


