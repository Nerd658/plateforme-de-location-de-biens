from django.urls import path
from . import views

urlpatterns = [
    path('reserver/<int:bien_id>/', views.reserver_bien, name='reserver_bien'),  # URL pour réserver un bien
    path('biens-reserves/', views.biens_reserves, name='biens_reserves'),
    path('annuler/<int:reservation_id>/', views.annuler_reservation, name='annuler_reservation'),

]   
