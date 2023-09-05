from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Attendance(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    morning_time = models.TimeField(null=True)
    evening_time = models.TimeField(null=True)
    punch_stat = models.TextField(max_length=50, null=True)
    punch_stat_evening = models.TextField(max_length=50, null=True)
    date = models.DateField(null=True)
    working_hour = models.CharField(max_length=50, null=True)
    difference = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.usr.username
    
    
class LeaveApplication(models.Model):
    empname = models.CharField(max_length=50, null=True)
    reason = models.CharField(max_length=100, null=True)
    approval = models.BooleanField(default=False, null=True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.empname
    
    
class rawmaterials(models.Model):
    rawmaterial_image = models.ImageField(upload_to="rawmaterial_image", null=True)
    rawmaterial_name = models.CharField(max_length=50, null=True)
    waight = models.CharField(max_length=50, null=True)
    numbers = models.IntegerField(null=True)
    rate = models.FloatField(null=True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.rawmaterial_name
    
    
class Products(models.Model):
    product_image = models.ImageField(upload_to="product_image", null=True)
    product_name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100,null=True)
    investment = models.FloatField(null=True)
    transportation_cost = models.FloatField(null=True)
    parcel_cost = models.FloatField(null=True)
    profit = models.FloatField(null=True)
    total_cost = models.FloatField(null=True)
    raw_material = models.ForeignKey(rawmaterials, on_delete=models.CASCADE,null=True,blank=True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.product_name
    
    
class ProjectManagement(models.Model):
    project_image = models.ImageField(upload_to="project_image", null=True)
    project_name = models.CharField(max_length=150, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE,null=True,blank=True)
    customer = models.CharField(max_length=100, null=True)
    raw_material = models.ForeignKey(rawmaterials, on_delete=models.CASCADE,null=True,blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    profit = models.FloatField(null=True)
    cotation = models.FloatField(null=True)
    
    def __str__(self):
        return self.project_name
    
    
class PersonWorkingOnProject(models.Model):
    name = models.CharField(max_length=50, null=True)
    project = models.ForeignKey(ProjectManagement, on_delete=models.CASCADE,null=True,blank=True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.name
    

class Tools(models.Model):
    tool_image = models.ImageField(upload_to="Tool_image", null=True)
    tool_name = models.CharField(max_length=50, null=True)
    quantity = models.IntegerField(null=True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.tool_name
    
    
class ProjectGroth(models.Model):
    text = models.CharField(max_length=250,null=True)
    date = models.DateField(null=True)
    usr = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    project = models.ForeignKey(ProjectManagement, on_delete=models.CASCADE,null=True,blank=True) 
    
    def __str__(self):
        return self.project.project_name