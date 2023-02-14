"""wscubetech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wscubetech import views

urlpatterns = [
    path('vishal/', admin.site.urls,name="admin"),
    path('',views.homePage,name="default"),
    path('About-us/',views.About,name="About"),
    path('Home/',views.Home,name="Home"),
    path('Course/',views.Course,name="Course"),
    path('calculator/',views.calculator,name="calculator"),
    path('evenodd/',views.evenodd),
    path('submitform/',views.submitform,name="submitform"),
    path('Course/<int:courseId>',views.CourseDetails),
    path('userform/',views.userform),
    path('redirect/',views.redirect),
    path('marksheet/',views.marksheet,name="marksheet"),
    path('demopage/',views.demopage,name="demopage"),
    path('newsDetails/<slug>',views.newsDetails,name="newsDetails")

]


