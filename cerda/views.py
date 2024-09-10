from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ignacio(request):
    return HttpResponse("este es el index de la app")

def garrido(request):
    return HttpResponse("esta es la bienvenida a la app, binevenido")