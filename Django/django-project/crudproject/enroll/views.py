import email
from turtle import isvisible
from wsgiref.util import request_uri

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from enroll.models import User
from .forms import StudentRegistration
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm, email = em, password = pw)
            reg.save()

            fm.save   
            # fm = StudentRegistration()
    else:
        fm = StudentRegistration()   
    stud = User.objects.all() 
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})



#this fuction will delete entries/data
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        pi.delete()
        print("delete was clicked")
        return HttpResponseRedirect('/')




#function for update data entrie
def update_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
       pi = User.objects.get(pk = id)
       fm = StudentRegistration(instance=pi)
      
       
                
    return render(request,"enroll/updatestudent.html",{'form':fm})

def updated(request):
    return render(request,'enroll/homepage.html')

