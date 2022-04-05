from unicodedata import name
from django.urls import path
from website.views import *

app_name = "website"

urlpatterns = [
    path('', Websiteindex, name="Websiteindex" ),
    path('Online_Form_Fill/', Online_Form_Fill, name="Online_Form_Fill" ),
    path('ExamResult/', ExamResult, name="ExamResult" ),
    path('noticesnews/', noticesnews, name="noticesnews" ),

]


