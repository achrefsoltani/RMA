from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listActifs"),
    path('<int:type>/', views.listByType, name="listActifType"),
  
]