from django.db import models
from django.db import models
from django.contrib.auth.models import User
from biens.models import Bien 

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('en_attente', 'En attente'),
        ('paye', 'Payé'),
    ]
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)  # L'utilisateur qui réserve
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)  # Le bien réservé
    date_reservation = models.DateTimeField(auto_now_add=True)  # Date de la réservation
    date_debut = models.DateField()  # Date de début de location
    date_fin = models.DateField()  # Date de fin de location

    def __str__(self):
        return f"Réservation de {self.utilisateur} pour {self.bien} du {self.date_debut} au {self.date_fin}"
