from django.urls import path
from . import views

urlpatterns = [
    path('', views.inscription, name='inscription'),  # Page d'inscription
    path('connexion/', views.connexion, name='connexion'),  # Page de connexion avec ta vue personnalisée
    path('deconnexion/', views.deconnexion, name='deconnexion'),  # Déconnexion
]
