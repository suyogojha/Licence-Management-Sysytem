from django.db import models

# Create your models here.
class OnlineLicenceForm(models.Model):
    bloodgroup = models.CharField(max_length=255, null=True,blank=True)
    citizenshipissuedistrict = models.CharField(max_length=255, null=True,blank=True)
    passportno = models.TextField(max_length=255, null=True,blank=True)
    citizenshipno = models.CharField(max_length=255, null=True,blank=True)
    dateofbirth = models.DateField(max_length=255, null=True,blank=True)
    firstname = models.CharField(max_length=255, null=True,blank=True)
    middlename = models.CharField(max_length=255, null=True,blank=True)
    lastname = models.CharField(max_length=255, null=True,blank=True)
    relationship = models.CharField(max_length=255, null=True,blank=True)
    occupation = models.CharField(max_length=255, null=True,blank=True)
    address = models.CharField(max_length=255, null=True,blank=True)
    zone = models.CharField(max_length=255, null=True,blank=True)
    email = models.EmailField(max_length=255, null=True,blank=True)
    contactno = models.BigIntegerField(null=True,blank=True)
    officecontactno = models.BigIntegerField(null=True,blank=True)
    licensecatagory = models.CharField(max_length=255, null=True,blank=True)
    uploaddocument = models.ImageField(upload_to="upload/image", null=True, blank=True)
    documenttype = models.CharField(max_length=255, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.firstname
    
    class Meta:
            db_table = 'Online Forms'
            
            

    
