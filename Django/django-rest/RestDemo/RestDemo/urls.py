
from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from rest_framework.urlpatterns import format_suffix_patterns 
from WebApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^employee/', views.EmployeeList.as_view()),
    path('studentData/<int:id>',views.student_details),
    path('studentData/',views.studet_all_data),
    path('Addstudent/',views.student_create),
    
]
 