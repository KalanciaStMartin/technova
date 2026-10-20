from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TypeProgramme, Programme, Module, Specialisation

@admin.register(TypeProgramme)
class TypeProgrammeAdmin(admin.ModelAdmin):
    list_display = ['nom', 'description']
    search_fields = ['nom']


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1


class SpecialisationInline(admin.TabularInline):
    model = Specialisation
    extra = 1


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ['nom', 'code', 'type_programme', 'duree', 'actif', 'date_creation']
    list_filter = ['type_programme', 'actif']
    search_fields = ['nom', 'code']
    prepopulated_fields = {'code': ('nom',)}
    inlines = [ModuleInline, SpecialisationInline]
    
    fieldsets = (
        ('Informations de base', {
            'fields': ('nom', 'code', 'type_programme', 'description', 'duree', 'image', 'ordre', 'actif')
        }),
        ('Fiche Pédagogique', {
            'fields': ('objectifs_generaux', 'objectifs_specifiques', 'prerequis', 'methodes_pedagogiques', 'evaluation', 'ressources', 'competences_visees', 'projet_final')
        }),
        ('Volume Horaire', {
            'fields': ('volume_horaire_min', 'volume_horaire_max')
        }),
    )


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['numero', 'titre', 'programme', 'duree']
    list_filter = ['programme']
    search_fields = ['titre']


@admin.register(Specialisation)
class SpecialisationAdmin(admin.ModelAdmin):
    list_display = ['nom', 'programme']
    list_filter = ['programme']
    search_fields = ['nom']