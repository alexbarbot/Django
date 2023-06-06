from django.db import models
from datetime import datetime
from django import forms
from django.utils import timezone
from django.urls import reverse
import computerApp.choices as choices

# Create your models here.
class Machine(models.Model):
    

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=20)
    etat = models.BooleanField(default=False)
    maintenanceDate = models.DateField(default = timezone.now())
    mach = models.CharField(max_length=32, choices=choices.TYPE, default='PC')
    ip = models.GenericIPAddressField(default='0.0.0.0')
    def __str__(self):
        return self.nom
    def delete(self):
        super().delete()

class Personnel(models.Model):

    TYPE = (
        ('Genre', ('Genre - à choisir ')),
        ('Homme', ('Homme ')),
        ('Femme', ('Femme ')),
        ('ND', ('ND - ne préfaire pas ce prononcer')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=10)
    maintenanceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length=16, choices= TYPE, default='Genre')
    mail = models.EmailField(editable=False,blank=True)
    def __str__(self):
        return self.nom
    def delete(self):
        super().delete()
    # def save_mail(self,*args, **kwargs):
    #     self.mail = f"{self.prenom.lower()}"




