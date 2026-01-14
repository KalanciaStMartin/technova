from django.db import models
from django.contrib.auth.models import User
from programmes.models import Programme

class Inscription(models.Model):
    """Inscription d'un étudiant"""
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('A', 'Autre'),
    ]
    
    LIEN_CHOICES = [
        ('PERE', 'Père'),
        ('MERE', 'Mère'),
        ('TUTEUR', 'Tuteur légal'),
    ]
    
    STATUT_CHOICES = [
        ('EN_ATTENTE', 'En attente'),
        ('ACCEPTE', 'Accepté'),
        ('REFUSE', 'Refusé'),
        ('FINALISE', 'Finalisé'),
    ]
    
    # Lien avec utilisateur (optionnel)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # Programme
    programme = models.ForeignKey(Programme, on_delete=models.SET_NULL, null=True)
    annee_academique = models.CharField(max_length=20, default='2025-2026')
    
    # Infos personnelles
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenoms = models.CharField(max_length=200, verbose_name="Prénoms")
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=200)
    nationalite = models.CharField(max_length=100, default="Haïtienne")
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    adresse = models.TextField()
    
    # Parent/Tuteur
    nom_parent = models.CharField(max_length=200)
    lien_parent = models.CharField(max_length=10, choices=LIEN_CHOICES)
    telephone_parent = models.CharField(max_length=20)
    email_parent = models.EmailField()
    profession_parent = models.CharField(max_length=100)
    
    # Parcours académique
    niveau_bac = models.CharField(max_length=100, verbose_name="Niveau BAC")
    serie_bac = models.CharField(max_length=50, verbose_name="Série")
    etablissement_bac = models.CharField(max_length=200, verbose_name="Établissement")
    annee_bac = models.IntegerField(verbose_name="Année d'obtention")
    resultat_bac = models.CharField(max_length=50, verbose_name="Résultat/Mention")
    etudes_superieures = models.TextField(blank=True, null=True, verbose_name="Études supérieures")
    
    # Statut
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='EN_ATTENTE')
    documents_confirmes = models.BooleanField(default=False)
    date_inscription = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    # Notes administratives (seulement visible par admin)
    notes_admin = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-date_inscription']
        verbose_name = "Inscription"
        verbose_name_plural = "Inscriptions"
    
    def __str__(self):
        return f"{self.prenoms} {self.nom} - {self.programme}"