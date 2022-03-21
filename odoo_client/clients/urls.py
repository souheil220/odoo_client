from django.urls import path

from . import views

urlpatterns = [
    path("clients", views.index, name="index"),
   
]