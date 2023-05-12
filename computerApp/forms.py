from django import forms
from django.core.exceptions import ValidationError

class AddMachineForm (forms.Form) : 

    nom = forms.CharField(required=True, label='Nom de la machine')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 6:
            raise ValidationError(("erreur de format pour le champ nom"))
        return data


class AddPersonnelForm (forms.Form) : 

    nom = forms.CharField(required=True, label='Nom du personnel')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) != 8:
            raise ValidationError(("erreur de format pour le champ nom"))
        return data