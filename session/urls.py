from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listSessions"),

    path('<str:pk>/choix', views.choix, name="detailSession"),
    path('<str:pk>/listActifs', views.listActifC, name="actifsSession"),
    path('<str:pk>/vuln', views.vulnerabilites, name="vulSession"),
    path('<str:pk>/menaces', views.menaces, name="menaceSession"),
    path('<str:pk>/traitement', views.traitement, name="traitementSession"),
    path('<str:pk>/rapport', views.rapport, name="rapportSession"),

    path('<str:pk>/', views.detail, name="detailSession"),
]