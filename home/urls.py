from django.urls import path
from home.views import *

app_name = "home"

urlpatterns = [
    path("Dashboard/", Dashboard, name="Dashboard"),
    path("profile/", Profile, name="Profile"),
    path("licencesearch/", Licence_search, name="Licence_search"),
    path("onlineform/", online_form, name="online_form"),
    path("rules/", Rules, name="Rules"),
    path("genlicence/", genlicence, name="genlicence"),
    path("TrialDateTime/", TrialDateTime, name="TrialDateTime"),

]


