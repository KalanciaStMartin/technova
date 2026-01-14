from django.contrib import admin
from .models import Inscription

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenoms', 'programme', 'email', 'telephone', 'statut', 'date_inscription']
    list_filter = ['statut', 'programme', 'sexe', 'annee_academique']
    search_fields = ['nom', 'prenoms', 'email', 'telephone']
    date_hierarchy = 'date_inscription'
    
    fieldsets = (
        ('Programme', {
            'fields': ('programme', 'annee_academique', 'statut')
        }),
        ('Informations personnelles', {
            'fields': ('nom', 'prenoms', 'sexe', 'date_naissance', 'lieu_naissance', 'nationalite', 'telephone', 'email', 'adresse')
        }),
        ('Parent/Tuteur', {
            'fields': ('nom_parent', 'lien_parent', 'telephone_parent', 'email_parent', 'profession_parent')
        }),
        ('Parcours académique', {
            'fields': ('niveau_bac', 'serie_bac', 'etablissement_bac', 'annee_bac', 'resultat_bac', 'etudes_superieures')
        }),
        ('Documents et notes', {
            'fields': ('documents_confirmes', 'notes_admin')
        }),
    )
    
    readonly_fields = ['date_inscription', 'date_modification']
    
    actions = ['accepter_inscription', 'refuser_inscription']
    
    def accepter_inscription(self, request, queryset):
        queryset.update(statut='ACCEPTE')
        self.message_user(request, f"{queryset.count()} inscription(s) acceptée(s).")
    accepter_inscription.short_description = "Accepter les inscriptions sélectionnées"
    
    def refuser_inscription(self, request, queryset):
        queryset.update(statut='REFUSE')
        self.message_user(request, f"{queryset.count()} inscription(s) refusée(s).")
    refuser_inscription.short_description = "Refuser les inscriptions sélectionnées"