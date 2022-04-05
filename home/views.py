from django.shortcuts import redirect, render,reverse
from django.http import HttpResponse, HttpResponseRedirect
from home.models import *
from django.contrib import messages
from website.models import *

# Create your models here.
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


def Profile(request):
    return render(request, "profile.html")




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



def online_form(request):
    data = OnlineLicenceForm.objects.all() 
    context = {
        "data": data,      
        }
    return render(request, "onlineform.html", context)



def Rules(request):
    if request.method == 'POST':
        rule = notices()
        notice = request.POST.get('notice')
        rule.notice = notice
        rule.save()
        return redirect('/Dashboard')  
        
    return render(request, "rules.html")



def genlicence(request):
    return render(request, "LicenceGenerate.html")

def TrialDateTime(request):
    data = examResult.objects.get(status='Passed')
    contex= {
        "data":data,
    }
    return render(request, "trialdate.html", contex)

