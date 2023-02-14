from email.mime import application
import json
from urllib import response
from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import get_object_or_404, render
from django.urls import is_valid_path
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer 
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io




class EmployeeList(APIView):
    def get(self,request):
        QuerySet = Employee.objects.all()
        serializer = EmployeeSerializer(QuerySet,many=True)
        return Response(serializer.data)

    def post(self):
        pass 

# model Object - single student data

def student_details(request,id):
        #python data
        stu  = Student.objects.get(id=id)
        print("stu Data  : ",stu)
        
        #converting it into json
        serializer = StudentSerializer(stu)
        print("serializer data  : ",serializer)

        #json data
        json_data  = JSONRenderer().render(serializer.data)
        print("serializer data : ",json_data)

        return HttpResponse(json_data,content_type='application/json')


def studet_all_data(request):

    #python data
    st_data = Student.objects.all()

    #converting it into json
    serializer = StudentSerializer(st_data,many=True)

    #json data
    json_data = JSONRenderer().render(serializer.data) 

    return HttpResponse(json_data,content_type='application/json')                     
    # return HttpResponse(JsonResponse(serializer.data,safe=False))/// method ||
 
@csrf_exempt
def student_create(request):
    
    # getting the data through post method
    if request.method =="POST":
        json_data = request.body              # .. got json data
        print("\njson_data get from client's request though post method :",json_data)
        stream    = io.BytesIO(json_data)
        print("\nstram : ",stream)
        pythondata= JSONParser().parse(stream)
        print("\npythondata",pythondata)
        serializer= StudentSerializer(data = pythondata)
        print("\nserialiaser",serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Row added in table'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data,content_type='application/json')     








