from django.db import models 
import uuid
from  manager.models import *
# Create your models here.


class PointCollection(models.Model): 
    name= models.CharField(max_length=25 ,blank=True ,  null=True) 
    adresse= models.CharField(max_length=25 ,blank=True ,  null=True)   
    add_date =  models.DateField(auto_now_add=True )  
    manager  =  models.ForeignKey(Admin ,  on_delete=models.CASCADE)