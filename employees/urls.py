from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("elist/", views.elist,name="elist"),
    path("elist/employee/<int:id>",views.details,name="details"),
    path("employee/edit/<int:id>",views.edit,name="edit"),
    path("add/",views.add,name="add"),
    path("delete/<int:id>",views.delete,name="delete"),
]