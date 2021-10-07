from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listActifs"),
    path('<str:type>/', views.listByType, name="listActifType"),
  
]