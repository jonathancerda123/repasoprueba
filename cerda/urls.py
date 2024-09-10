from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.ignacio),
    path('bienvenida/', views.garrido),
]