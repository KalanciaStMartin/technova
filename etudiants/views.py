from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Inscription
from programmes.models import Programme

def inscription(request):
    if request.method == 'POST':
        # On récupère les données du formulaire
        inscription = Inscription(
            programme_id=request.POST.get('programme'),
            nom=request.POST.get('nom'),
            prenoms=request.POST.get('prenoms'),
            sexe=request.POST.get('sexe'),
            date_naissance=request.POST.get('date_naissance'),
            lieu_naissance=request.POST.get('lieu_naissance'),
            nationalite=request.POST.get('nationalite'),
            telephone=request.POST.get('telephone'),
            email=request.POST.get('email'),
            adresse=request.POST.get('adresse'),
            nom_parent=request.POST.get('nom_parent'),
            lien_parent=request.POST.get('lien_parent'),
            telephone_parent=request.POST.get('telephone_parent'),
            email_parent=request.POST.get('email_parent'),
            profession_parent=request.POST.get('profession_parent'),
            niveau_bac=request.POST.get('niveau_bac'),
            serie_bac=request.POST.get('serie_bac'),
            etablissement_bac=request.POST.get('etablissement_bac'),
            annee_bac=request.POST.get('annee_bac'),
            resultat_bac=request.POST.get('resultat_bac'),
            etudes_superieures=request.POST.get('etudes_superieures'),
            documents_confirmes=request.POST.get('documents_confirmes') == 'on',
        )
        inscription.save()
        messages.success(request, 'Votre pré-inscription a été enregistrée avec succès!')
        return redirect('inscription_success')
    
    programmes = Programme.objects.filter(actif=True)
    return render(request, 'etudiants/inscription.html', {
        'programmes': programmes,
        'annee': '2025-2026'
    })

def inscription_success(request):
    return render(request, 'etudiants/inscription_success.html')