from django.db import models 
import uuid
from  manager.models import *
# Create your models here.


class PointCollection(models.Model): 
    id =  models.UUIDField(default =  uuid.uuid4() , primary_key=True , unique=True)
    name= models.CharField(max_length=25 ,blank=True ,  null=True) 
    adresse= models.CharField(max_length=25 ,blank=True ,  null=True)   
    add_date =  models.DateField(auto_now_add=True )  
    manager  =  models.ForeignKey(Admin ,  on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + " "  + self.name 
     