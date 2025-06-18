from django.shortcuts import render
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("HOLA Barckl3y - CI/CD CON NOTIFICAICONES EN GITHUB ACTIONS")
