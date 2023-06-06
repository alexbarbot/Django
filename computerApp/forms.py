from django import forms
from django.core.exceptions import ValidationError
from .models import Machine, Personnel
from datetime import datetime, timezone
import computerApp.choices as choices

class DateInput(forms.DateInput):
    input_type = 'date'
    
class AddMachineForm (forms.Form) : 
    
    maintenanceDate = forms.DateField(widget=DateInput, label='Date de maintenance')
    nom = forms.CharField(required=True, label='Nom de la machine')
    mach = forms.ChoiceField(choices=choices.TYPE, label='Type')
    etat = forms.BooleanField(required=False, label="état de la machine")
    ip = forms.GenericIPAddressField(label='Adresse IP')
    #appart = forms.ModelChoiceField(queryset=Personnel.objects.all(),required=True, label="appartient à ")
   
    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 20:
            raise ValidationError(("erreur de format pour le champ nom"))
        return data
    
    def clean_maintenanceDate(self):
        data = self.cleaned_data["maintenanceDate"]
        if data < datetime.today().date():
            raise ValidationError(_("Erreur de format pour le champ maintenanceDate"))
        return data
    
    def cleaned_ip(self):
        data = self.cleaned_data["ip"]
        regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        if not (re.search(regex, data)):
            raise ValidationError(_("Erreur de format pour le champ maintenanceDate"))
        return data
    
    def cleaned_mach(self):
        data = self.cleaned_data["mach"]
        if data not in choices.TYPE:
            raise ValidationError(_("Erreur de format pour le champ maintenanceDate"))
        return data

class AddPersonnelForm (forms.Form) : 

    nom = forms.CharField(required=True, label='Nom du personnel')
    mail = forms.EmailField(max_length=50, label = 'nom du mail')
    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 10:
            raise ValidationError(("erreur de format pour le champ nom"))
        return data
    
    def clean_mail(self):
        data = self.cleaned_data["mail"]
        if len(data) > 20:
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
