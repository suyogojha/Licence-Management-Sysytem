
from django.db import models



class examResult(models.Model):
    Passed = "Passed"
    Fail = "Fail"
    Absent = "Absent"
    class_type = (
        (Passed, 'Passed'),
        (Fail, 'Fail'),
        (Absent, 'Absent'),
    )
    applicantid = models.CharField(max_length=255, null=True,blank=True)
    applicantname = models.CharField(max_length=255, null=True,blank=True)
    fathername = models.CharField(max_length=255, null=True,blank=True)
    citizenshipno = models.CharField(max_length=255, null=True,blank=True)
    category = models.CharField(max_length=255, null=True,blank=True)
    status = models.CharField(choices=class_type, max_length=255)         

    def __str__(self):
        return self.applicantname
    
class trialdate(models.Model):
    name = models.ForeignKey(examResult, on_delete=models.CASCADE,null=True, blank=True)
    trialdatetime = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.location
    
    
    
class notices(models.Model):
    notice = models.CharField(max_length=255, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.notice   