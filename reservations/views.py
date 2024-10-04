from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from biens.models import Bien  # Importer le modèle Bien

@login_required
def reserver_bien(request, bien_id):
    # Récupérer le bien par son ID
    bien = get_object_or_404(Bien, id=bien_id)

    # Si la méthode est POST, cela signifie que l'utilisateur a soumis le formulaire
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Créer une réservation mais ne pas l'enregistrer encore
            reservation = form.save(commit=False)
            reservation.utilisateur = request.user  # Associer la réservation à l'utilisateur connecté
            reservation.bien = bien  # Associer la réservation au bien
            reservation.save()  # Enregistrer la réservation dans la base de données

            # Rediriger vers la page "Mes biens" après une réservation réussie
            return redirect('mes_biens')  # Change cela en fonction de ton URL de redirection
    else:
        # Si la méthode n'est pas POST, créer une nouvelle instance de formulaire
        form = ReservationForm()

    # Rendre le template avec le formulaire et le bien
    return render(request, 'reservations/reserver_bien.html', {'form': form, 'bien': bien})

@login_required
def biens_reserves(request):
    # Récupérer toutes les réservations faites par l'utilisateur connecté
    reservations = Reservation.objects.filter(utilisateur=request.user)

    context = {
        'reservations': reservations,
    }
    return render(request, 'reservations/biens_reserves.html', context)