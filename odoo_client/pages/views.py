from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import re
from .sql import connexion_ad2000, connexion_email

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect("clients/")
    return render(request, "pages/login.html")


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        pass_django = "Azerty@22"
        if not re.match(r"^[A-Za-z0-9\.\+-]+@[A-Za-z0-9\.-]+\.[a-zA-Z]*$", username):
            email_util = "GROUPE-HASNAOUI\\" + username
            connexion = connexion_ad2000(email_util, password)
        else:
            connexion = connexion_email(username, password)

        print("connexion ", connexion)
        if connexion == "deco":
            messages.error(request, "AD/Email ou PASSWORD erroné")
            context = {"failed": True, "messages": "AD/Email ou PASSWORD erroné"}
            return render(request, "pages/login.html", context)
        else:
            user = authenticate(
                request, username=connexion["ad_2000"], password=pass_django
            )
            if user is None:
                user = User.objects.create_user(
                    connexion["ad_2000"], connexion["mail"], pass_django
                )
            print("user ", user)

            if user is not None:
                login(request, user)
                return redirect("index")

            else:
                messages.error(request, "Accès non autorisé")
                context = {"failed": True, "messages": "Utilisateur Innéxistant"}
                render(request, "pages/login.html", context)
    else:
        return render(request, "pages/login.html")


def logoutUser(request):
    print("logout")
    logout(request)
    return redirect("login")
