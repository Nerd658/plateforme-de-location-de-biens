# paiement/views.py
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import stripe

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

@csrf_exempt
def process_payment(request):
    if request.method == 'POST':
        try:
            # Créez un paiement
            charge = stripe.Charge.create(
                amount=5000,  # Montant en cents (ici 50,00 €)
                currency='eur',
                source=request.POST['stripeToken'],
                description='Paiement pour une réservation',
            )
            return redirect('success')  # Redirigez vers une page de succès
        except stripe.error.StripeError as e:
            # Gérer les erreurs
            return redirect('error')  # Redirigez vers une page d'erreur
    return render(request, 'paiement.html')

# paiement/views.py
def success(request):
    return render(request, 'success.html')

def error(request):
    return render(request, 'error.html')
