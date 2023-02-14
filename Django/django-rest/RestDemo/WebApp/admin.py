from django.contrib import admin

# Register your models here.
from .models import Employee,Student

admin.site.register(Employee)
# admin.site.register(Student)


#another method
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= ['id','RollNo','Name','City']