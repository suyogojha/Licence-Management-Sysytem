from django.contrib import admin
from home.models import *

# Register your models here.
@admin.register(examResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ("applicantid","applicantname", "fathername", "citizenshipno", "category","status")
    list_filter = ("applicantid","applicantname", "fathername", "citizenshipno", "category","status")
    search_fields = ["applicantid","applicantname", "fathername", "citizenshipno", "category","status"]  


@admin.register(notices)
class noticesAdmin(admin.ModelAdmin):
    list_display = ("notice","created")
    list_filter = ("notice", "created")
    search_fields = ["notice", "created"]
    
    
@admin.register(trialdate)
class trialdateAdmin(admin.ModelAdmin):
    list_display = ("name","trialdatetime", "location")
    list_filter = ("name", "trialdatetime")
    search_fields = ["name", "trialdatetime"]