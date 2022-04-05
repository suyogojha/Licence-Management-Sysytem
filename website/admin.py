from django.contrib import admin
from website.models import  *

# Register your models here.
@admin.register(OnlineLicenceForm)
class OnlineLicenceFormAdmin(admin.ModelAdmin):
    list_display = ("bloodgroup","citizenshipissuedistrict", "passportno", "citizenshipno", "dateofbirth","firstname","middlename","lastname","relationship","occupation","address","zone","email","contactno","officecontactno","licensecatagory","uploaddocument","documenttype")
    list_filter = ("bloodgroup", "citizenshipno", "firstname", "licensecatagory")
    search_fields = ["bloodgroup", "citizenshipno", "firstname", "licensecatagory"]  

