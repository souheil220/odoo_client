from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect("clients/clients")
    return render(request, "pages/login.html")


def loginPage(request):
    return render(request, "pages/login.html")


def logoutUser(request):
    logout(request)
    return redirect("login")
