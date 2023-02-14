from __future__ import division
from pickle import TRUE
from re import T
from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersForm
from service.models import Service
from news.models import news
from django.core.paginator import Paginator


def homePage(request):
    data = {
        'title': "home new title",
        'bdata': "courses",
        'clist': ['php','java','django'],
        'student_details':[
            {'name':'vishal','phone':2349782389},
            {'name':'pranav','phone':4212112389}
                           ],
        'numbers':[]
    }
    return render(request,"index.html",data)


def About(request): 
    return HttpResponse("welcome it is about page")

def Home(request):
    return HttpResponse("It is home page")   

def Course(request):
    return HttpResponse("It is course page")    

def CourseDetails(request,courseId):
    return HttpResponse(courseId)











def userform(request):
    
    finalans=0
    fn = usersForm()
    data={'form' : fn}
    try:
        if request.method=="POST":
       
        # n1=int(request.GET['num1'])
        # n2=int(request.GET['num2'])
        
         n1=int(request.POST.get('num1'))
         n2=int(request.POST.get('num2'))
         finalans = n1 + n2
         data={'form' : fn,
               'output' : finalans
            }
         url="/redirect/?output={}".format(finalans)
         return redirect(url)


    except:    pass
    return render(request,"userform.html")











def redirect(request):
    if request.method=='GET':
        output=request.GET.get('output')

    return render(request,"redirect.html",{'output':output})










def submitform(request): 
    try:
        if request.method=="POST":
       
        # n1=int(request.GET['num1'])
        # n2=int(request.GET['num2'])
        
         n1=int(request.POST.get('num1'))
         n2=int(request.POST.get('num2'))
         finalans = n1 + n2
         data={'n1':n1,
               'n2':n2,
               'output' : finalans
            }
          
         return HttpResponse(finalans)
    except:    pass
    




def calculator(request):
    c=''
    try: 
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                c=n1+n2
            elif opr == "-":
                c=n1-n2
            elif opr == "*":
                c = n1*n2
            elif opr =="/":
                c= n1/n2

    except:
        c="invalid opr...."
    print(c)    
    return render(request,"calculator.html",{'c':c})




def evenodd(request):
    c=''
    
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request,"evenodd.html",{'error':True})
        n = eval(request.POST.get('num1'))
        if n%2== 0:
            c = "Even number"
        else: 
            c= "Odd number"    
    return render(request,"evenodd.html",{'c':c})





def marksheet(request):
    s1=''
    s2=''
    s3=''
    s4=''
    s5=''
    t=''
    percent=''
    division=''

    if request.method == "POST":
         s1 = eval(request.POST.get('sub1'))
         s2 = eval(request.POST.get('sub2'))
         s3 = eval(request.POST.get('sub3'))
         s4 = eval(request.POST.get('sub4'))
         s5 = eval(request.POST.get('sub5'))
         t = s1+s2+s3+s4+s5
         percent = t/5

         print(t)
         print(percent)
         if percent >=90:
            division="A"
         elif percent >=80 and percent<90:
            division = "B"   
         elif percent >=70 and percent<80:
            division = "C"   
         elif percent >=60 and percent<70:
            division = "D"   
         elif percent >=50 and percent<60:
            division = "E" 
         elif percent <50:
            division = "F"
         print(division)    

    return render(request,"marksheet.html",{'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'t':t,'percent':percent,'division':division})     





#  geting the data from table to the html page
def demopage(request):
    serviceData = Service.objects.all()     #  serviceData = Service.objects.all().order_by('-id')[:3]     # gives descending order  for ascending order dont use '-' sign to fieldname , [] --> we can  limit the entries i.e. slice the entris
    paginator = Paginator(serviceData,3)
    page_number = request.GET.get('page')
    serviceDatafinal = paginator.get_page(page_number)
    totalPage = serviceDatafinal.paginator.num_pages
    if request.method=="GET":
        st = request.GET.get('servicename')
        if st!= None: 
            serviceData = Service.objects.filter(service_title__icontains=st)      # __icontains  use for filter the data ,if we search on a letter it shows or gives result da containing that letter

    newsData = news.objects.all()
    # for n in serviceData:
    #     print(n.service_icon)     -----> gives the service_icons from the database table
    data = {'serviceData':serviceDatafinal,
             'newsData':newsData,
             'last page': totalPage}
    return render(request,"demopage.html",data)



def newsDetails(request,slug):
    newsDetails = news.objects.get(news_slug=slug)
    print("news Id:",slug)
    data = {'newsDetails':newsDetails}
    return render(request,"newsDetails.html",data)
