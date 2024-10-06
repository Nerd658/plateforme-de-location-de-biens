from django.shortcuts import render , redirect , get_object_or_404
from .models import Bien
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import BienForm
# Create your views here.


# Vue pour afficher la liste de tous les biens disponibles
def liste_biens(request):
    biens = Bien.objects.filter(disponibilite=True) 
    print(biens)# On affiche uniquement les biens disponibles
    return render(request, 'biens/liste_biens.html', {'biens': biens})

# Vue pour afficher les biens créés par l'utilisateur connecté
@login_required 
def mes_biens(request):
    biens = Bien.objects.filter(utilisateur=request.user)  # Filtrer les biens de l'utilisateur connecté
    return render(request, 'biens/mes_biens.html', {'biens': biens})

@login_required
def creer_bien(request):
    
    categories = Bien.CATEGORIES 
    
    if request.method == 'POST':
        titre = request.POST['titre']
        description = request.POST['description']
        prix = request.POST['prix']
        categorie = request.POST['categorie']
        photo = request.FILES['photo']  # Récupérer le fichier photo
        date_debut_disponibilite = request.POST['date_debut']
        date_fin_disponibilite = request.POST['date_fin']

        # Créer le bien
        Bien.objects.create(
            titre=titre,
            description=description,
            prix=prix,
            categorie=categorie,
            photo=photo,
            utilisateur=request.user,  # Associer le bien à l'utilisateur connecté
            date_debut_disponibilite=date_debut_disponibilite,
            date_fin_disponibilite=date_fin_disponibilite,
            disponibilite=True  # Par défaut, le bien est disponible
        )

        messages.success(request, 'Bien créé avec succès!')
        return redirect('acceuil')  # Redirige vers la page d'accueil après la création

    return render(request, 'biens/creer_bien.html' ,  {'categories': categories})  # Afficher le formulaire de création





# Vue pour modifier un bien
@login_required
def modifier_bien(request, bien_id):
    bien = get_object_or_404(Bien, id=bien_id)

    if request.method == 'POST':
        form = BienForm(request.POST, request.FILES, instance=bien)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bien modifié avec succès.')
            return redirect('mes_biens')
    else:
        form = BienForm(instance=bien)

    return render(request, 'biens/modifier_bien.html', {'form': form, 'bien': bien})

# Vue pour supprimer un bien
@login_required
def supprimer_bien(request, bien_id):
    bien = get_object_or_404(Bien, id=bien_id)
    
    if request.method == 'POST':
        bien.delete()
        messages.success(request, 'Bien supprimé avec succès.')
        return redirect('mes_biens')

    return render(request, 'biens/supprimer_bien.html', {'bien': bien})
