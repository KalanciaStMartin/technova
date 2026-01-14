from django.contrib import admin
from .models import Evenement

@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display = ['titre', 'date_debut', 'date_fin', 'lieu', 'a_la_une', 'archive']
    list_filter = ['a_la_une', 'archive', 'date_debut']
    search_fields = ['titre', 'description', 'lieu']
    date_hierarchy = 'date_debut'