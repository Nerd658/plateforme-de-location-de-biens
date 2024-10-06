from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from biens.models import Bien  # Importer le modèle Bien
from django.contrib import messages  # Pour afficher des messages d'erreur ou de succès

@login_required
def reserver_bien(request, bien_id):
    bien = get_object_or_404(Bien, id=bien_id)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Récupérer les dates de la réservation
            date_debut = form.cleaned_data['date_debut']
            date_fin = form.cleaned_data['date_fin']
            
            # Vérifier les conflits de dates
            if date_debut >= date_fin:
                messages.error(request, "La date de début doit être avant la date de fin. Veuillez corriger les dates.")
            else:
                # Vérifier les conflits de dates
                conflits = Reservation.objects.filter(
                    bien=bien,
                    date_debut__lte=date_fin,  # Si la date de début de la réservation existante est avant la fin de la nouvelle réservation
                    date_fin__gte=date_debut    # Si la date de fin de la réservation existante est après le début de la nouvelle réservation
                )
            
                if conflits.exists():
                    # Si un conflit est trouvé, afficher un message d'erreur
                    messages.error(request, "Ce bien est déjà réservé pour les dates sélectionnées. Veuillez choisir d'autres dates.")
                else:
                    # Si pas de conflit, on enregistre la réservation
                    reservation = form.save(commit=False)
                    reservation.utilisateur = request.user
                    reservation.bien = bien
                    reservation.save()
                    messages.success(request, "Réservation effectuée avec succès!")
                return redirect('biens_reserves')  # Redirection vers une page qui montre les réservations de l'utilisateur
    else:
        form = ReservationForm()

    return render(request, 'reservations/reserver_bien.html', {'form': form, 'bien': bien})

@login_required
def biens_reserves(request):
    # Récupérer toutes les réservations faites par l'utilisateur connecté
    reservations = Reservation.objects.filter(utilisateur=request.user)

    context = {
        'reservations': reservations,
    }
    return render(request, 'reservations/biens_reserves.html', context)

@login_required
def annuler_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id, utilisateur=request.user)
    
    # On supprime la réservation
    reservation.delete()
    
    messages.success(request, "Réservation annulée avec succès!")
    return redirect('biens_reserves')  # Redirection vers la page des réservation