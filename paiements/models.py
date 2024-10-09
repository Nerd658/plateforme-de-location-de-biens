# paiements/models.py

from django.db import models
from django.contrib.auth.models import User
from reservations.models import Reservation

class Paiement(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)  # L'utilisateur qui a effectué le paiement
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)  # Réservation associée au paiement
    montant = models.DecimalField(max_digits=10, decimal_places=2)  # Montant payé
    statut = models.CharField(max_length=20)  # Statut du paiement

    def __str__(self):
        return f"Paiement de {self.utilisateur} pour {self.reservation.bien.titre} de {self.montant}€"
