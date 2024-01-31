from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse #Papildome imports
from django.contrib.auth.models import User
import datetime


from django.urls import reverse #Papildome imports

class Uzrasai(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    createdtime = models.DateTimeField(verbose_name='Data', auto_now_add=True)
    tekstas = models.TextField(verbose_name="Tekstas", max_length=3000, help_text='Užrašai')
    def __str__(self):
        return self.tekstas