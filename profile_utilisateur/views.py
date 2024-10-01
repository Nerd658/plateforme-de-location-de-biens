from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from django.shortcuts import redirect

from django.shortcuts import get_object_or_404

# Create your views here.

@login_required
def acceuil(request):
    return render(request, 'profile_utilisateur/acceuil.html') 

@login_required
def profile(request):
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
    return render(request, 'profile_utilisateur/profile.html', {
        'form': form,
        'profile': profile  # Envoi du profil à afficher dans la page
    })
