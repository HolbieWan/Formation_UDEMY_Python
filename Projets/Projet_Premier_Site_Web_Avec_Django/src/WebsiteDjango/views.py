# from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):
    print("Bonjour")
    date = datetime.today()
    print(date)
    return render(request, "index.html", context={
        "prenom": "Cedric",
        "date": date},
                  )
