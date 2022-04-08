from django.shortcuts import redirect, render,reverse
from django.http import HttpResponse, HttpResponseRedirect
from home.models import *
from django.contrib import messages
from website.models import *
from django.contrib.auth.decorators import login_required

# Create your models here.
@login_required(login_url='login:Login')
def Dashboard(request):
    data = OnlineLicenceForm.objects.all().count()
    data2 = examResult.objects.all().count()
    data3 = notices.objects.all().count()
    
    
    conte = {
        "data":data,
        "data2":data2,
        "data3":data3,
    }

    return render(request, "Dashboard.html", conte)

@login_required(login_url='login:Login')
def Profile(request):
    return render(request, "profile.html")



@login_required(login_url='login:Login')
def Licence_search(request):
    if request.method =='POST':
            exam = examResult()
            applicantid = request.POST.get('applicantid')
            applicantname = request.POST.get('applicantname')
            fathername = request.POST.get('fathername')
            citizenshipno = request.POST.get('citizenshipno')
            category = request.POST.get('category')
            status = request.POST.get('status')
            exam.applicantid = applicantid
            exam.applicantname = applicantname
            exam.fathername = fathername
            exam.citizenshipno = citizenshipno
            exam.category = category
            exam.status = status
            exam.save()
            messages.success(request, 'Contact request submitted successfully.')
            return redirect('/Dashboard')  
    return render(request, "licencesearch.html")


@login_required(login_url='login:Login')
def online_form(request):
    data = OnlineLicenceForm.objects.all() 
    context = {
        "data": data,      
        }
    return render(request, "onlineform.html", context)


@login_required(login_url='login:Login')
def Rules(request):
    if request.method == 'POST':
        rule = notices()
        notice = request.POST.get('notice')
        rule.notice = notice
        rule.save()
        return redirect('/Dashboard')  
        
    return render(request, "rules.html")






@login_required(login_url='login:Login')
def genlicence(request):
    return render(request, "LicenceGenerate.html")



@login_required(login_url='login:Login')
def TrialDateTime(request):
    if request.method == 'POST':
        tri = trialdate()
        trialdatetime = request.POST.get('trialdatetime')
        location = request.POST.get('location')
        tri.trialdatetime = trialdatetime
        tri.location = location
        tri.save()
        return redirect('/Dashboard')  
    return render(request, "trialdatetimeh.html")

