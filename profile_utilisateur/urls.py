from django.urls import path

from . import views

urlpatterns = [
    path('acceuil/', views.acceuil, name='acceuil'),  # Route pour la page d'accueil
    path('profile/', views.profile, name='profile'),  # Route pour le profil
   
]
