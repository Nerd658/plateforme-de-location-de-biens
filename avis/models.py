from django.db import models
from django.contrib.auth.models import User
from biens.models import Bien

# Create your models here.

class Avis(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    texte = models.TextField()
    note = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Note de 1 à 5
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Avis de {self.utilisateur.username} sur {self.bien.titre}'
