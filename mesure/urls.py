from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listMesures"),

    path('add/', views.ajoutMesure, name="addMesure"),
    path('update/<str:pk>/', views.updateMesure, name="updateMesure"),
]