from django.urls import path
from . import views

urlpatterns = [
    path('ajouter/<int:bien_id>/', views.ajouter_avis, name='ajouter_avis'),
    path('supprimer/<int:avis_id>/', views.supprimer_avis, name='supprimer_avis'),
]
