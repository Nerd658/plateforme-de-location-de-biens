from django import forms
from .models import Avis

class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ['note', 'texte']
        widgets = {
            'note': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'texte': forms.Textarea(attrs={'rows': 4}),
        }
