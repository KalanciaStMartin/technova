from django.db import models

class Evenement(models.Model):
    """Événements (InnovTech, conférences, remises diplômes...)"""
    titre = models.CharField(max_length=200)
    description = models.TextField()
    lieu = models.CharField(max_length=300)
    
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    
    image = models.ImageField(upload_to='evenements/', blank=True)
    lien_inscription = models.URLField(blank=True)
    lien_youtube = models.URLField(blank=True)  # Pour YouTube Live
    
    a_la_une = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)
    
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_debut']
        verbose_name = "Événement"
        verbose_name_plural = "Événements"
    
    def __str__(self):
        return self.titre