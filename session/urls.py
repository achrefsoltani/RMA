from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listSessions"),
    path('new', views.new, name="NouvelleSession"),
    path('addM/<str:pk>/<str:pka>', views.addMes, name="addMes"),


    path('ac/<str:pk>/add/<str:pka>', views.addAc, name="addAc"),
    path('ac/<str:pk>/del/<str:pka>', views.delAc, name="delAc"),
    path('ac/<str:pk>/fin/<str:pka>', views.finAc, name="finAc"),

    path('ac/<str:pk>/v', views.VulAc, name="VulAc"),
    path('ac/<str:pk>/v/<str:pkv>/del', views.delVul, name="delVul"),

    path('ac/<str:pk>/M', views.MenAc, name="MenAc"),
    path('ac/<str:pks>/M/<str:pki>/del', views.delMen, name="delMen"),

    path('<str:pk>/choix', views.choixAc, name="choixAc"),
    path('<str:pk>/listAc', views.listAc, name="listAc"),
    path('<str:pk>/traitement', views.traitement, name="traitementSession"),
    path('<str:pk>/plan', views.plan, name="planSession"),

    path('<str:pk>/', views.detail, name="detailSession"),
    path('<str:pk>/del', views.delSess, name="deleteSession"),


    
]