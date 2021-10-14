from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name="profile"),
    path('signin', views.auth, name="signin"),
    path('logout', views.logout_user, name="logout"),
]