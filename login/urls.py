from django.urls import path
from login.views import *

app_name = "login"

urlpatterns = [
    path("login/", Login, name="Login"),
    path("signup/", Signup, name="Signup"),
    path("logoutUser/", logoutUser, name="logoutUser"),

]


