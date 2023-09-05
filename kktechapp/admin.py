from django.contrib import admin
from .models import Tools, Attendance, LeaveApplication, rawmaterials, Products, ProjectGroth, ProjectManagement, PersonWorkingOnProject 

# Register your models here.

admin.site.register(Attendance)
admin.site.register(LeaveApplication)
admin.site.register(rawmaterials)
admin.site.register(Products)
admin.site.register(ProjectGroth)
admin.site.register(ProjectManagement)
admin.site.register(PersonWorkingOnProject)
admin.site.register(Tools)