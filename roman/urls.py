from django.urls import path
from . import views

urlpatterns = [
    path('', views.danitza),
    path('sepulveda/', views.sepulveda)
]
