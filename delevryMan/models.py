from django.db import models

# Create your models here.

class DeliveryMan(models.Model):
    firstNameDeliverer= models.CharField(null=False, max_length=30)
    lastNameDeliverer= models.TextField(null=False)
    phoneDeliverer= models.BigIntegerField(null=False)
    emailDeliverer= models.EmailField(null=False)
    
    class Meta:
        db_table= 'table_deliveryMan'