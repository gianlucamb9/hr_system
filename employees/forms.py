from django import forms
from django.forms import ModelForm
from .models import Employee

class EmpRegForm(forms.Form):
    fname = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class":"form-control","fname":"fname","placeholder":"Enter first name"}))
    lname = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class":"form-control","lname":"lname","placeholder":"Enter last name"}))
    email = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class":"form-control","email":"email","placeholder":"Enter email"}))
    phone = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class":"form-control","phone":"phone","placeholder":"Enter phone"}))
    department = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class":"form-control","department":"department","placeholder":"Enter department"}))
    year = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class":"form-control","year":"year","placeholder":"Enter year of hire"}))
    salary = forms.CharField(max_length=60, widget=forms.TextInput(attrs={"class":"form-control","salary":"salary","placeholder":"Enter base salary"}))

class EmpEditForm(ModelForm):
    class Meta:
        model = Employee
        fields = ("fname", "lname", "email", "phone", "department", "year", "salary")

        widgets = {
            "fname":forms.TextInput(attrs={"class":"form-control","fname":"fname","placeholder":"Enter first name"}),
            "lname":forms.TextInput(attrs={"class":"form-control","lname":"lname","placeholder":"Enter last name"}),
            "email":forms.TextInput(attrs={"class":"form-control","email":"email","placeholder":"Enter email"}),
            "phone":forms.TextInput(attrs={"class":"form-control","phone":"phone","placeholder":"Enter phone"}),
            "department":forms.TextInput(attrs={"class":"form-control","department":"department","placeholder":"Enter department"}),
            "year":forms.TextInput(attrs={"class":"form-control","year":"year","placeholder":"Enter year of hire"}),
            "salary":forms.TextInput(attrs={"class":"form-control","salary":"salary","placeholder":"Enter base salary"})
        }