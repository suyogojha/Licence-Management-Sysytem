from django.shortcuts import redirect, render,reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your models here.
def Login(request):
    return render(request, "loginpage.html")


def Signup(request):
    return render(request, "LoginSignup.html")
