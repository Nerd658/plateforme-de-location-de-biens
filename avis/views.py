from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Avis
from .forms import AvisForm
from biens.models import Bien
from django.contrib.auth.decorators import login_required

@login_required
def ajouter_avis(request, bien_id):
    bien = get_object_or_404(Bien, id=bien_id)
    
    if request.method == 'POST':
        form = AvisForm(request.POST)
        if form.is_valid():
            avis = form.save(commit=False)
            avis.utilisateur = request.user
            avis.bien = bien
            avis.save()
            return redirect('detail_bien', bien_id=bien.id)  # Rediriger vers la page du bien
    else:
        form = AvisForm()

    return render(request, 'avis/ajouter_avis.html', {'form': form, 'bien': bien})

@login_required
def supprimer_avis(request, avis_id):
    avis = get_object_or_404(Avis, id=avis_id, utilisateur=request.user)
    
    # Supprimer l'avis seulement si l'utilisateur est celui qui a posté l'avis
    if request.method == 'POST':
        avis.delete()
        messages.success(request, "Avis supprimé avec succès.")
        return redirect('detail_bien', bien_id=avis.bien.id)  # Rediriger vers la page du bien

    return render(request, 'avis/supprimer_avis.html', {'avis': avis})