# paiements/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create-checkout-session/<int:reservation_id>/', views.creer_session_paiement, name='creer_session_paiement'),
    path('success/<int:reservation_id>/', views.paiement_reussi, name='paiement_reussi'), 
    path('cancel/', views.paiement_annule, name='paiement_annule'),
]
