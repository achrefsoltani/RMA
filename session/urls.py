from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="listSessions"),
    path('details/', views.details, name="detailsSessions"),
]