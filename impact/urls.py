from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listImpacts"),

    path('add/', views.ajoutImpact, name="addimpact"),
    path('update/<str:pk>/', views.updateImpact, name="updateImpact"),
]