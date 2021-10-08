from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listSessions"),

    path('choix', views.choix, name="choixAcSession"),
    path('choix/<str:pk>', views.ajoutActifC, name="AjoutActifC"),

    path('listActifs/<str:pk>', views.listActifC, name="actifsSession"),
    path('vuln/<str:pk>', views.vulnerabilites, name="vulSession"),
    path('menaces/<str:pk>', views.menaces, name="menaceSession"),
    path('traitement/<str:pk>', views.traitement, name="traitementSession"),
    path('rapport/<str:pk>', views.rapport, name="rapportSession"),

    path('<str:pk>/', views.detail, name="detailSession"),


]