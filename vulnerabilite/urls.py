from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listVulnerabilites"),

    path('add/', views.ajoutVulnerabilite, name="addVulnerabilite"),
    path('update/<str:pk>/', views.updateVulnerabilite, name="updateVulnerabilite"),
]