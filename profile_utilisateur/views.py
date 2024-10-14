from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from django.shortcuts import redirect
from reservations.models import Reservation
from biens.models import Bien
from django.shortcuts import get_object_or_404

# Create your views here.

# @login_required
# def acceuil(request):
#     return render(request, 'raccourcis/base.html')  ceci etait un test

@login_required
def profile(request):
    # Récupérer le profil de l'utilisateur connecté, le créer si nécessaire
    
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    # Compter les réservations et les biens
    reservations = Reservation.objects.filter(utilisateur=request.user)
    biens = Bien.objects.filter(utilisateur=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('acceuil')  # Redirige vers la page d'accueil après mise à jour
    else:
        form = ProfileForm(instance=profile)

    # Affiche le formulaire et les informations actuelles de l'utilisateur
    return render(request, 'profile_utilisateur/profile.html', {
        'form': form,
        'profile': profile,
        'nombre_reservations': reservations.count(),
        'nombre_biens': biens.count(),
        'reservations': reservations,
        'biens': biens,
    })
    
# partis pour la mise a jour
@login_required
def mise(request):
    # Récupérer le profil de l'utilisateur connecté, le créer si nécessaire
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('acceuil')  # Redirige vers la page d'accueil après mise à jour
    else:
        form = ProfileForm(instance=profile)

    # Affiche le formulaire et les informations actuelles de l'utilisateur
    return render(request, 'profile_utilisateur/mise.html', {
        'form': form,
        'profile': profile  # Envoi du profil à afficher dans la page
    })
