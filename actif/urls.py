from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listActifs"),

    path('add/', views.ajoutActif, name="addActif"),
    path('update/<str:pk>/', views.updateActif, name="updateActif"),


]