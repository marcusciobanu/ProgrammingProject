from django.urls import path
from . import views

# Manages URL patterns for landing page, login page and registration
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login/", views.loginpage, name="loginpage"),
    path("register/", views.registerpage, name="registerpage"),
]
