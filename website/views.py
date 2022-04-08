from django.shortcuts import redirect, render,reverse
from django.http import HttpResponse, HttpResponseRedirect
from website.models import *
from django.contrib import messages
from home.models import *


# Create your models here.
def Websiteindex(request):
    data = notices.objects.all()
    contex = {
        "data":data,
    }
    return render(request, "weblic.html", contex)

def noticesnews(request):
    data = notices.objects.all()
    contex = {
        "data":data,
    }
    return render(request, "notices.html", contex)


def Online_Form_Fill(request):
    data = OnlineLicenceForm.objects.all().count()
    if request.method =='POST':
            onform = OnlineLicenceForm()
            bloodgroup = request.POST.get('bloodgroup')
            citizenshipissuedistrict = request.POST.get('citizenshipissuedistrict')
            passportno = request.POST.get('passportno')
            citizenshipno = request.POST.get('citizenshipno')
            dateofbirth = request.POST.get('dateofbirth')
            firstname = request.POST.get('firstname')
            middlename = request.POST.get('middlename')
            lastname = request.POST.get('lastname')
            relationship = request.POST.get('relationship')
            occupation = request.POST.get('occupation')
            address = request.POST.get('address')
            zone = request.POST.get('zone')
            email = request.POST.get('email')
            contactno = request.POST.get('contactno')
            officecontactno = request.POST.get('officecontactno')
            licensecatagory = request.POST.get('licensecatagory')
            uploaddocument = request.POST.get('uploaddocument')
            documenttype = request.POST.get('documenttype')
            onform.bloodgroup = bloodgroup
            onform.citizenshipissuedistrict = citizenshipissuedistrict
            onform.passportno = passportno
            onform.citizenshipno = citizenshipno
            onform.dateofbirth = dateofbirth
            onform.firstname = firstname
            onform.middlename = middlename
            onform.lastname = lastname
            onform.relationship = relationship
            onform.occupation = occupation
            onform.address = address
            onform.zone = zone
            onform.email = email
            onform.contactno = contactno
            onform.officecontactno = officecontactno
            onform.licensecatagory = licensecatagory
            onform.uploaddocument = uploaddocument
            onform.documenttype = documenttype
            onform.save()
            messages.success(request, 'Contact request submitted successfully.')
            return redirect('/')
    context = {
        'data':data,
    }
    return render(request, "fillonlineform.html", context)




def ExamResult(request):
    data = examResult.objects.all()
    context = {
        "data":data,
               }
      
    return render(request, "examresult.html", context)


def LocationOFTrial(request):
    data = trialdate.objects.all()
    context = {
        "data":data,
               }
      
    return render(request, "Trialdatetime.html", context)





