from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def danitza(request):
    html = """
    <h1>Hola, Danitza</h1>
    """
    return HttpResponse(html)

def sepulveda(request):
    html = """
    <h2>Hola, Sepúlveda</h2>
    """
    return HttpResponse(html)
