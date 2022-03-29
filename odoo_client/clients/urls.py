from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detailClient/<str:id>", views.detailClient, name="detailClient"),
    path("modifierClient", views.modifierClient, name="modifierClient"),
]
