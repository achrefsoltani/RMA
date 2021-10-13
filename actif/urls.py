from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listActifs"),

    path('type/add/', views.ajoutTypeActif, name="addTypeActif"),
    path('type/update/<str:pk>/', views.updateTypeActif, name="updateTypeActif"),

    path('critique/add/', views.ajoutActifCritique, name="addActifCritique"),
    path('critique/update/<str:pk>/', views.updateActifCritique, name="updateActifCritique"),

    path('add/', views.ajoutActif, name="addActif"),
    path('update/<str:pk>/', views.updateActif, name="updateActif"),
    path('delete/<str:pk>/', views.deleteActif, name="deleteActif")




    
  
]