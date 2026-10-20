from django.contrib import admin
from .models import CategorieRessource, Ressource

@admin.register(CategorieRessource)
class CategorieRessourceAdmin(admin.ModelAdmin):
    list_display = ['nom', 'icone']


@admin.register(Ressource)
class RessourceAdmin(admin.ModelAdmin):
    list_display = ['titre', 'categorie', 'auteur', 'acces_restreint', 'telechargements', 'date_ajout']
    list_filter = ['categorie', 'acces_restreint', 'date_ajout']
    search_fields = ['titre', 'auteur', 'mots_cles']
    date_hierarchy = 'date_ajout'