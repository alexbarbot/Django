from django.db import models
from datetime import datetime
from django import forms


# Create your models here.
class Machine(models.Model):
    
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Server', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=10)
    #etat = forms.BooleanField(required=True, label="état de la machine")
    maintenanceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length=32, choices= TYPE, default='PC')
    #appart = forms.ModelChoiceField(queryset=Personnel.objects.all(),required=True, label="appartient à ")
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

    # id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=10)
    maintenanceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length=16, choices= TYPE, default='Genre')
    def __str__(self):
        return self.nom
    def delete(self):
        super().delete()




