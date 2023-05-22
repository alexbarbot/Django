from django import forms
from django.core.exceptions import ValidationError
from .models import Machine, Personnel

TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Server', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
    )
class AddMachineForm (forms.Form) : 
    
    nom = forms.CharField(required=True, label='Nom de la machine')
    type = forms.ChoiceField(choices=TYPE, label='Type')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 8:
            raise ValidationError(("erreur de format pour le champ nom"))
        return data

class AddPersonnelForm (forms.Form) : 

    nom = forms.CharField(required=True, label='Nom du personnel')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 10:
            raise ValidationError(("erreur de format pour le champ nom"))
        return data

class DeleteMachineForm(forms.Form):
    machines = forms.ModelMultipleChoiceField(
        queryset=Machine.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class DeletePersonnelForm(forms.Form):
    personnels = forms.ModelMultipleChoiceField(
        queryset=Personnel.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
