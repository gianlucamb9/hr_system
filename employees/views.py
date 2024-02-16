from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Employee
from . import forms
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())

@login_required
@permission_required("employees.can_edit", raise_exception=True)
def register(request):
    template = loader.get_template("resgiter.html")
    return HttpResponse(template.render())

@login_required
@permission_required("employees.can_view", raise_exception=True)
def elist(request):
    elist = Employee.objects.all().values()
    pageTemp = loader.get_template("elist.html")
    context = {
        "elist":elist,
    }
    return HttpResponse(pageTemp.render(context,request))

@login_required
@permission_required("employees.can_view", raise_exception=True)
def details(request,id):
    employee = Employee.objects.get(id=id)
    pageTemp = loader.get_template("details.html")
    context = {
        "employee":employee
    }
    return HttpResponse(pageTemp.render(context,request))

@login_required
@permission_required("employees.can_edit", raise_exception=True)
def add(request):
    form = forms.EmpRegForm()
    errMsg = ""
    if request.method == "POST":
        form = forms.EmpRegForm(request.POST)
        if form.is_valid():
            emp = Employee(
                fname = form.cleaned_data["fname"],
                lname = form.cleaned_data["lname"],
                email = form.cleaned_data["email"],
                phone = form.cleaned_data["phone"],
                department = form.cleaned_data["department"],
                year = form.cleaned_data["year"],
                salary = form.cleaned_data["salary"],
            )
            emp.save()
            return redirect("elist")
        else:
            errMsg = "An error ocurred."
    context = {
        "form":form,
        "errMsg":errMsg
    }
    return render(request,"add.html",context)


@login_required
@permission_required("employees.can_edit", raise_exception=True)
def delete(request,id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect("elist")

@login_required
@permission_required("employees.can_edit", raise_exception=True)
def edit(request, id):
    emp = Employee.objects.get(id=id)
    form = forms.EmpEditForm(request.POST or None, instance=emp)
    if form.is_valid():
        form.save()
        return redirect("elist")
    context = {
        "form":form
    }
    return render(request,"edit.html", context)


# Create your views here.
