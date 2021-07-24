from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listImpacts"),

    path('add/', views.ajoutImpact, name="addimpact")
]