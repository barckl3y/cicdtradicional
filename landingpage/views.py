from django.shortcuts import render
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("<h1>Hola Mundo CI CD TRADICIONAL con GITHUB ACTIONS</h1>")
