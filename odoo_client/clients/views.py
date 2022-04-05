from multiprocessing.dummy.connection import Client
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .sql import SQLConnexion
from .models import *
from django.core.cache import cache
from django.http import Http404
from datetime import datetime

# Create your views here.
@login_required(login_url="login")
def index(request):
    database = SQLConnexion(
        user="cbiuser",
        password="CBI@2022.GSHR",
        host="10.20.10.18",
        port="5434",
        database="hasnaoui",
    )
    list = database.connection()

    # r = redis.Redis(host=os.environ.get("CASH_HOST"), port=os.environ.get("CASH_PORT"))
    # print(r.dbsize())
    # print(cache.dbsize())
    keys = []
    data = []
    if len(cache.keys("*")) > 0:
        keys = cache.keys("*")
        for key in keys:
            data.append(cache.get(key))
        print("cache get")
        redis_cache = True
    else:
        data = database.get_bad_clients(list[0])
        for i in range(0, len(data)):
            client = Client(
                id=data[i][0],
                name=data[i][1],
                x_rc=data[i][2],
                x_nif=data[i][3],
                x_nis=data[i][4],
                x_art=data[i][5],
                is_person=data[i][6],
                x_is_professional_non_commercial=None,
                x_professional_identity_ref=None,
                x_identity_ref_delevery_date=None,
                x_identity_refissuing8quthority=None,
            )
            cache.set(client.id, client, 3600000)
        print("cache set")
        redis_cache = False
        print(data[0][0])
    database.closeConnection(list[0], list[1])
    context = {"penalite": len(data) * 5000, "data": data, "cache": redis_cache}
    return render(request, "clients/index.html", context)


def detailClient(request, id):
    if request.is_ajax and request.method == "GET":
        clientDetail = cache.get(int(id))
        context = {"id": id, "client": clientDetail}
        return render(request, "clients/clientDetails.html", context)
    else:
        raise Http404


def modifierClient(request):
    if request.method == "POST":
        id = request.POST.get("id_client_selected")
        database = SQLConnexion(
            user="cbiuser",
            password="CBI@2022.GSHR",
            host="10.20.10.18",
            port="5434",
            database="hasnaoui",
        )
        list = database.connection()
        id = request.POST.get("id_client_selected")
        rc = request.POST.get("rc")
        nif = request.POST.get("nif")
        nis = request.POST.get("nis")
        art = request.POST.get("art")
        if request.POST.get("est_particulier", False) == "on":
            est_particulier = True
            if request.POST.get("professional_non_commercial", False) == "on":
                professional_non_commercial = True
                id_pro = request.POST.get("ID_pro")
                id_date = datetime.strptime(request.POST.get("ID_date"), "%Y-%m-%d")
                id_authority = request.POST.get("ID_authority")
                input_ID = "NULL"
            else:
                professional_non_commercial = False
                input_ID = request.POST.get("input_ID")
        else:
            est_particulier = False
            professional_non_commercial = False
            id_pro = "NULL"
            id_date = "NULL"
            id_authority = "NULL"
            input_ID = "NULL"

        database.update_client_infos(
            list[0],
            list[1],
            rc,
            nif,
            nis,
            art,
            professional_non_commercial,
            id_pro,
            id_authority,
            id_date,
            input_ID,
            est_particulier,
            id,
        )

        database.closeConnection(list[0], list[1])
        return redirect("clients/")
