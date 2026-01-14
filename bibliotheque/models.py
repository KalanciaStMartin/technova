from django.db import models

class CategorieRessource(models.Model):
    """Type de ressource: Livre, Vidéo, Document, Article..."""
    nom = models.CharField(max_length=100)
    icone = models.CharField(max_length=50, blank=True)  # Ex: "fa-book"
    
    def __str__(self):
        return self.nom


class Ressource(models.Model):
    """Ressources de la bibliothèque"""
    titre = models.CharField(max_length=200)
    categorie = models.ForeignKey(CategorieRessource, on_delete=models.CASCADE)
    auteur = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    
    # Fichier ou lien
    fichier = models.FileField(upload_to='bibliotheque/', blank=True)
    lien_externe = models.URLField(blank=True)
    
    image_couverture = models.ImageField(upload_to='bibliotheque/covers/', blank=True)
    
    # Mots-clés pour recherche
    mots_cles = models.CharField(max_length=300, blank=True)
    
    acces_restreint = models.BooleanField(default=True)  # Réservé aux étudiants?
    telechargements = models.IntegerField(default=0)
    
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titre