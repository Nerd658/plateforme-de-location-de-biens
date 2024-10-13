# biens/admin.py
from django.contrib import admin
from .models import Bien

@admin.register(Bien)
class BienAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'prix', 'disponibilite', 'date_debut_disponibilite', 'date_fin_disponibilite')
    search_fields = ('titre', 'categorie')
    list_filter = ('disponibilite', 'categorie')
