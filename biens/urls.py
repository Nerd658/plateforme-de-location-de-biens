from django.urls import path
from . import views

urlpatterns = [
    path('liste/', views.liste_biens, name='liste_biens'),
    path('mes_biens/', views.mes_biens, name='mes_biens'),
    path('creer/', views.creer_bien, name='creer_bien'), # Créer un bien
    path('modifier/<int:bien_id>/', views.modifier_bien, name='modifier_bien'),
    path('supprimer/<int:bien_id>/', views.supprimer_bien, name='supprimer_bien'),
]