from django.shortcuts import render
from django.http import HttpResponse

from .models import Planet


def home(request):
    for p in Planet.objects.all():
        print(f'line: {p}')
    return HttpResponse("<h1>Home Page</h1>")


def planets_detail(request, planet_id):
    # if request.method == GET:
    return HttpResponse(f"<p>Viewing detail of Planet with id: {planet_id} </p>")