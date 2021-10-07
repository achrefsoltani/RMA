from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listVulnerabilites"),

    path('type/add/', views.ajoutTypeVulnerabilite, name="addTypeVulnerabilite"),
    path('type/update/<str:pk>/', views.updateTypeVulnerabilite, name="updateTypeVulnerabilite"),

    path('note/add/', views.ajoutVulnerabiliteNote, name="addVulnerabiliteNote"),
    path('note/update/<str:pk>/', views.updateVulnerabiliteNote, name="updateVulnerabiliteNote"),



    path('add/', views.ajoutVulnerabilite, name="addVulnerabilite"),
    path('update/<str:pk>/', views.updateVulnerabilite, name="updateVulnerabilite"),
    path('delete/<str:pk>/', views.deleteVulnerabilite, name="deleteVulnerabilite")

]