from django import forms
from django.core.exceptions import ValidationError
from .models import Machine, Personnel
from datetime import datetime, timezone, time
import computerApp.choices as choices
import re

class DateInput(forms.DateInput):
    input_type = 'date'

class AddMachineForm(forms.Form):
    maintenanceDate = forms.DateField(widget=DateInput, label='Date de maintenance')
    nom = forms.CharField(required=True, label='Nom de la machine')
    mach = forms.ChoiceField(choices=choices.TYPE, label='Type')
    etat = forms.BooleanField(required=False, label="État de la machine")
    ip = forms.GenericIPAddressField(label='Adresse IP')
    appart = forms.ModelChoiceField(queryset=Personnel.objects.all(), required=True, label="Appartient à")

    def clean_nom(self):
        # Validation du champ "nom" pour s'assurer qu'il ne dépasse pas 20 caractères
        data = self.cleaned_data["nom"]
        if len(data) > 20:
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data

    def clean_maintenanceDate(self):
        # Validation du champ "maintenanceDate" pour s'assurer qu'il est supérieur ou égal à la date actuelle
        data = self.cleaned_data["maintenanceDate"]
        #.strftime('%Y-%m-%d')
        today_datetime = datetime.today().date()
        if data < today_datetime:
            raise ValidationError((f"Erreur de format pour le champ maintenanceDate, {data}, {datetime.today().date()}"))
        return data

    def clean_ip(self):
        # Validation du champ "ip" pour s'assurer qu'il correspond au format d'une adresse IP valide
        data = self.cleaned_data["ip"]
        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        if not (re.search(regex, data)):
            raise ValidationError(("Erreur de format pour le champ IP"))
        return data

    def clean_mach(self):
        # Validation du champ "mach" pour s'assurer qu'il correspond à une valeur valide parmi les choix disponibles
        data = self.cleaned_data["mach"]
        if data not in [choice[0] for choice in choices.TYPE]:
            raise ValidationError(("Erreur de format pour le champ machine"))
        return data
    
    def clean_appart(self):
        # Validation du champ "appart" pour s'assurer qu'une valeur valide a été sélectionnée
        data = self.cleaned_data["appart"]
        if data is None:
            raise ValidationError(("Erreur de format pour le champ appart"))
        return data


class AddPersonnelForm(forms.Form):
    nom = forms.CharField(required=True, label='Nom du personnel')
    mail = forms.EmailField(max_length=50, label='Nom du mail')

    def clean_nom(self):
        # Validation du champ "nom" pour s'assurer qu'il ne dépasse pas 10 caractères
        data = self.cleaned_data["nom"]
        if len(data) > 10:
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data

    def clean_mail(self):
        # Validation du champ "mail" pour s'assurer qu'il ne dépasse pas 20 caractères
        data = self.cleaned_data["mail"]
        if len(data) > 20:
            raise ValidationError(("Erreur de format pour le champ nom"))
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
