from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listImpacts"),

    path('type/add/', views.ajoutTypeImpact, name="addTypeImpact"),
    path('type/update/<str:pk>/', views.updateTypeImpact, name="updateTypeImpact"),

    path('note/add/', views.ajoutImpactNote, name="addImpactNote"),
    path('note/update/<str:pk>/', views.updateImpactNote, name="updateImpactNote"),



    path('add/', views.ajoutImpact, name="addimpact"),
    path('update/<str:pk>/', views.updateImpact, name="updateImpact"),
    path('delete/<str:pk>/', views.deleteImpact, name="deleteImpact")

]