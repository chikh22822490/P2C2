from django.db import models
from user.models import Account
from django.forms import ValidationError
from datetime import date
# from .services import client_clean_email
from django.utils import timezone


class Client(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    telephone = models.CharField(max_length=250, blank=True, null=True)
    add_date = models.DateField(auto_now_add=True, blank=True, null=True)

    def get_full_name(self):
        return self.last_name + " " + self.first_name

    '''
    def clean(self):
        if date.today().year - self.birthday.year > 18:
            raise ValidationError("The client age is not correct")'''

    def __str__(self):
        return str(self.id) + " " + self.get_full_name()
