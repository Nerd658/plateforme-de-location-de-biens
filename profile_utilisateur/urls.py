from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('acceuil/', views.acceuil, name='acceuil'),  # Route pour la page d'accueil
    path('profile/', views.profile, name='profile'),  # Route pour le profil
    path('mise/', views.mise, name='mise'), 
   
]
