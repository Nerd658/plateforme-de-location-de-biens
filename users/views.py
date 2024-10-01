from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from profile_utilisateur.views import acceuil 
import re

# Create your views here.

#ici cest pour la partie dinscription qui utlise le formulaire que nous avons personaliser users/forms.py


# users/views.py
import re
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        # Récupération des données directement de request.POST
        username = request.POST.get("username")
        email = request.POST.get("email")  # Assurez-vous d'avoir un champ email dans le formulaire
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Vérifications
        if User.objects.filter(username=username).exists():
            messages.error(request, "Un utilisateur avec ce nom existe déjà.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Un utilisateur avec cet e-mail existe déjà.")
        elif len(password1) < 8:
            messages.error(request, "Le mot de passe doit contenir au moins 8 caractères.")
        elif not re.search(r"\d", password1) or not re.search(r"[A-Za-z]", password1):
            messages.error(request, "Le mot de passe doit être un mélange de chiffres et de lettres.")
        elif password1 != password2:
            messages.error(request, "Veuillez renseigner les mêmes mots de passe.")
        elif form.is_valid():  # Validation du formulaire
            user = form.save(commit=False)  # Ne pas sauvegarder tout de suite
            user.email = email  # Assurez-vous d'enregistrer l'email
            user.save()  # Maintenant, sauvegardez l'utilisateur
            messages.success(request, "Inscription réussie !")
            return redirect('connexion')

    else:
        form = UserCreationForm()

    return render(request, 'users/inscription.html', {'form': form})




def connexion(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        username = request.POST['username']
        password = request.POST['password']

        # Authentification de l'utilisateur
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Si l'authentification est réussie, on connecte l'utilisateur
            login(request, user)
            messages.success(request, "Connexion réussie.")
            return redirect ('acceuil') # Redirection vers la page d'accueil après la connexion
        else:
            # Si l'authentification échoue, on affiche un message d'erreur
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    # Si c'est une requête GET ou que l'authentification échoue, on affiche le template de connexion
    return render(request, 'users/connexion.html')


def deconnexion (request) :
    return render (request , "users/deconnexion.html")