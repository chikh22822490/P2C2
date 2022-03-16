from django.db import models

# Create your models here.

class Farmer(models.Model):
    firstNameFarmer= models.CharField(null=False, max_length=30)
    lastNameFarmer= models.TextField(null=False)
    phoneFarmer= models.BigIntegerField(null=False)
    emailFarmer= models.EmailField(null=False)
    adressFarmer= models.TextField(null=False) 
    class Meta:
        db_table= 'table_farmer'




