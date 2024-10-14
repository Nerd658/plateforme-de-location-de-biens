from django.shortcuts import render

from django.utils import timezone
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from reservations.models import Reservation


STRIPE_TEST_SECRET_KEY = "sk_test_51Q7rWk2Ml1214h57UFVr3RYVGGC5XsHnECZwTILaa0gdPMjoRR0XXJN9e8Tmhy5TVpNIKUNULtgjahotyr7bQXFA002aHZinFb"

stripe.api_key = STRIPE_TEST_SECRET_KEY  # Configurer la clé API Stripe

@login_required
def creer_session_paiement(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    
    # Montant à payer (en centimes)
    montant = int(reservation.bien.prix * 100)  # Convertir en centimes

    # Créer une session de paiement Stripe
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'xof',
                'product_data': {
                    'name': reservation.bien.titre,
                },
                'unit_amount': montant,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(f'/paiements/success/{reservation.id}/') + '?session_id={CHECKOUT_SESSION_ID}',

        cancel_url=request.build_absolute_uri('/paiements/cancel/'),
    )

    return redirect(session.url, code=303)  # Rediriger vers la session de paiement


# paiements/views.py

def paiement_reussi(request, reservation_id):
    # Récupérer la réservation pour mise à jour (si nécessaire)
    reservation = get_object_or_404(Reservation, id=reservation_id)

    # Mettre à jour la date de paiement
    reservation.date_paiement = timezone.now()  # Définit la date de paiement à maintenant
    reservation.save()  # Sauvegarde les modifications

    # Rediriger vers la page des réservations
    return redirect('biens_reserves') 



def paiement_annule(request):
    return render(request, 'paiements/cancel.html')
