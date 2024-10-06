from django import forms
from .models import Bien

class BienForm(forms.ModelForm):
    class Meta:
        model = Bien
        fields = ['titre', 'description', 'prix', 'categorie', 'photo', 'date_debut_disponibilite', 'date_fin_disponibilite', 'disponibilite']
