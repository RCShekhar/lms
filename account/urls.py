from django.urls import path
from . import views

urlpatterns = [
    path("registration/", views.register, name="register"),
    #path("login", views.registration, name="login"),
    #path("logout", views.registration, name="logout"),
    path("", views.register, name="default")
]