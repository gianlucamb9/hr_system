from django.db import models

class Employee(models.Model):
    fname = models.CharField(max_length=50, verbose_name="First name")
    lname = models.CharField(max_length=50, verbose_name="Last name")
    email = models.CharField(max_length=50, verbose_name="Email")
    phone = models.CharField(max_length=12, verbose_name="Phone")
    department = models.CharField(max_length=100, verbose_name="Department")
    year = models.CharField(max_length=4, verbose_name="Year of hire")
    salary = models.CharField(max_length=8,verbose_name="Salary")

    class Meta:
        permissions = (("can_view","View employees"),("can_edit", "Edit employees"))

    def __str__(self):
        return f"{self.fname} {self.lname}"
    
    @property
    def rsalary(self):
        salary = int(self.salary)
        year = int(self.year)
        eyears= 2024-year
        return int(salary + (salary*0.05*eyears))

# Create your models here.
