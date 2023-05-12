from django.db import models
from datetime import datetime

# Create your models here.
class Machine(models.Model):
    
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Server', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=6)
    maintenanceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length=32, choices= TYPE, default='PC')
    
    """"
    id = models.AutoField(
                    primary_key=True,
                    editable=False)
    nom= models.CharField(
                max_length= 6)
    def __str__ (self):
        return str(self.id) + " -> " + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom
    """


class Personnel(models.Model):

    TYPE = (
        ('Genre', ('Genre - à choisir ')),
        ('Homme', ('Homme ')),
        ('Femme', ('Femme ')),
        ('ND', ('ND - ne préfaire pas ce prononcer')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=8)
    maintenanceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length=16, choices= TYPE, default='Genre')

    """
    id = models.AutoField(
                    primary_key=True,
                    editable=False)
    nom= models.CharField(
                max_length= 8)
    prenom = models.CharField(
                max_length= 16)
    def __str__ (self):
        return str(self.id) + " -> " + self.nom

    def get_name(self):
        return str(self.id) + " " + self.nom
    
    def __str__ (self):
        return str(self.id) + " -> " + self.prenom

    def get_name(self):
        return str(self.id) + " " + self.prenom
    """






