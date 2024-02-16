from django.shortcuts import render,redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth import authenticate,login

class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

def Login_View(request):
    form = forms.LoginForm()
    errMsg = ""
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"],
            )
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                errMsg = "Username/Password does not exist."
    context = {
        "form":form,
        "errMsg":errMsg
    }
    return render(request,"registration/login.html",context)

def reset_view(request):
    form = forms.PassResetForm()
    if request.method == "POST":
        form = forms.PassResetForm(request.POST)
        if form.is_valid():
            return redirect("password_reset_done")
    context = {
        "form":form
    }
    return render(request, "registration/password_reset.html", context)

# Create your views here.
