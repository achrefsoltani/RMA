from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listMenaces"),

    path('add/', views.ajoutMenace, name="addMenace"),
    path('update/<str:pk>/', views.updateMenace, name="updateMenace"),
    
]