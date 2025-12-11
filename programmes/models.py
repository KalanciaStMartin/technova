from django.db import models

# Create your models here.


class TypeProgramme(models.Model):
    """Type de formation: Diplôme, Certificat, Séminaire"""
    nom = models.CharField(max_length=100)  # Ex: "Formation longue", "Formation courte"
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Type de Programme"
        verbose_name_plural = "Types de Programmes"
    
    def __str__(self):
        return self.nom


class Programme(models.Model):
    """Un programme de formation (ex: DUT Informatique, Licence...)"""
    nom = models.CharField(max_length=200)  # Ex: "DUT en Informatique"
    code = models.CharField(max_length=50, unique=True)  # Ex: "DUT-INFO"
    type_programme = models.ForeignKey(TypeProgramme, on_delete=models.CASCADE)
    description = models.TextField()
    duree = models.CharField(max_length=100)  # Ex: "2 ans", "6 mois"
    
    # Infos de la fiche pédagogique
    objectifs_generaux = models.TextField()
    objectifs_specifiques = models.TextField()
    prerequis = models.TextField(blank=True)
    methodes_pedagogiques = models.TextField()
    evaluation = models.TextField()  # Comment on évalue l'étudiant
    ressources = models.TextField()  # Outils utilisés
    competences_visees = models.TextField()
    projet_final = models.TextField(blank=True)
    
    # Volume horaire
    volume_horaire_min = models.IntegerField(default=0)  # Heures minimum
    volume_horaire_max = models.IntegerField(default=0)  # Heures maximum
    
    image = models.ImageField(upload_to='programmes/', blank=True)
    ordre = models.IntegerField(default=0)  # Pour trier
    actif = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['ordre', 'nom']
        verbose_name = "Programme"
        verbose_name_plural = "Programmes"
    
    def __str__(self):
        return self.nom


class Module(models.Model):
    """Les modules d'un programme (ex: Module 1: Introduction...)"""
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='modules')
    numero = models.IntegerField()  # Numéro du module
    titre = models.CharField(max_length=200)
    description = models.TextField()
    duree = models.CharField(max_length=100, blank=True)  # Ex: "2 semaines"
    
    class Meta:
        ordering = ['numero']
        verbose_name = "Module"
    
    def __str__(self):
        return f"Module {self.numero}: {self.titre}"


class Specialisation(models.Model):
    """Spécialisations d'un programme (ex: Administration réseaux, Dev d'applis)"""
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, related_name='specialisations')
    nom = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.nom