from django.contrib import admin
from .models import CategorieArticle, Article

@admin.register(CategorieArticle)
class CategorieArticleAdmin(admin.ModelAdmin):
    list_display = ['nom', 'slug']
    prepopulated_fields = {'slug': ('nom',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['titre', 'categorie', 'auteur', 'publie', 'a_la_une', 'date_publication', 'vues']
    list_filter = ['publie', 'a_la_une', 'categorie', 'date_publication']
    search_fields = ['titre', 'contenu']
    prepopulated_fields = {'slug': ('titre',)}
    date_hierarchy = 'date_publication'
    
    fieldsets = (
        ('Contenu', {
            'fields': ('titre', 'slug', 'categorie', 'auteur', 'contenu', 'image')
        }),
        ('Publication', {
            'fields': ('publie', 'a_la_une', 'date_publication')
        }),
    )
    
    readonly_fields = ['vues']