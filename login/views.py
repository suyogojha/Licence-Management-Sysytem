from django.shortcuts import redirect, render,reverse
from django.http import HttpResponse, HttpResponseRedirect


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from login.decorators import *
# Create your models here.


def Signup(request):
    return render(request, "LoginSignup.html")





@unauthenticated_user
def Login(request):	
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
            
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            return redirect('home:Dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')
    
    context = {} 
    return render(request, "loginpage.html", context)
 
 
 
def logoutUser(request):
	logout(request)
	return redirect('login:Login')
