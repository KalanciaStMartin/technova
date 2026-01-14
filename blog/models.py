from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class CategorieArticle(models.Model):
    """Catégories d'articles (Actualités, Tech, Success Stories...)"""
    nom = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.nom


class Article(models.Model):
    """Articles du blog/actualités"""
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    categorie = models.ForeignKey(CategorieArticle, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    contenu = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True)
    
    publie = models.BooleanField(default=False)
    a_la_une = models.BooleanField(default=False)  # Pour page d'accueil
    
    date_creation = models.DateTimeField(auto_now_add=True)
    date_publication = models.DateTimeField(null=True, blank=True)
    vues = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-date_publication']
        verbose_name = "Article"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.titre