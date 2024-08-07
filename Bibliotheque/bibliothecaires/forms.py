from django import forms
from .models import Membre

class Creationmembre(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['nom']  # Assurez-vous que les champs sont corrects
