from django.shortcuts import render
from django.http import HttpResponse

def hola_mundo(request):
    return HttpResponse("<h1>HOLA MUNDO CON CI/CD CON GITHUB ACTIONS 18 de junio 2025 -v3 CON NOTIFICACIONES EMAIL</h1>")
