from django.contrib import admin
from .models import Employee

class EmployeesModelView(admin.ModelAdmin):
    list_display = ("fname", "lname", "email", "phone", "department", "year", "salary")

admin.site.register(Employee,EmployeesModelView)

# Register your models here.
