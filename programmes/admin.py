from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TypeProgramme, Programme, Module, Specialisation

@admin.register(TypeProgramme)
class TypeProgrammeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'code', 'type_programme', 'actif', 'ordre')
    list_filter = ('type_programme', 'actif')
    search_fields = ('nom', 'code')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'programme', 'numero')
    list_filter = ('programme',)
    search_fields = ('titre',)

@admin.register(Specialisation)
class SpecialisationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'programme')
    list_filter = ('programme',)
    search_fields = ('nom',)
