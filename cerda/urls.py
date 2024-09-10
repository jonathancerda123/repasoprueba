from django.urls import path
from . import views

urlpatterns = [
    path('', views.ignacio),
    path('bienvenida/', views.garrido),
]