from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone

from .models import Evenement


def evenements_liste(request):
    """
    Affiche la liste des événements avec filtres :
    - tous (défaut)
    - a-venir
    - a-la-une
    - archives
    """
    filtre = request.GET.get('filtre', 'tous')
    maintenant = timezone.now()

    # Querysets de base pour les stats du hero (toujours calculés sur l'ensemble)
    evenements_a_venir = Evenement.objects.filter(
        archive=False, date_debut__gte=maintenant
    )
    evenements_archives = Evenement.objects.filter(archive=True)
    evenements_une = Evenement.objects.filter(a_la_une=True, archive=False)

    # Événement vedette : le plus proche parmi ceux marqués "à la une"
    evenement_vedette = evenements_une.filter(
        date_debut__gte=maintenant
    ).order_by('date_debut').first()

    if not evenement_vedette:
        # Fallback : le plus récent marqué à la une, même s'il est passé
        evenement_vedette = evenements_une.order_by('-date_debut').first()

    # Queryset filtré pour la grille
    if filtre == 'a-venir':
        queryset = evenements_a_venir.order_by('date_debut')
    elif filtre == 'a-la-une':
        queryset = evenements_une.order_by('-date_debut')
    elif filtre == 'archives':
        queryset = evenements_archives.order_by('-date_debut')
    else:
        filtre = 'tous'
        queryset = Evenement.objects.all().order_by('-date_debut')

    # Pagination
    paginator = Paginator(queryset, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'evenements': page_obj,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'evenement_vedette': evenement_vedette,
        'evenements_a_venir': evenements_a_venir,
        'evenements_archives': evenements_archives,
        'evenements_une': evenements_une,
        'total_evenements': Evenement.objects.count(),
        'filtre': filtre,
    }
    return render(request, 'evenements/evenements.html', context)


def evenement_detail(request, pk):
    """Affiche le détail d'un événement."""
    evenement = get_object_or_404(Evenement, pk=pk)
    context = {
        'evenement': evenement,
    }
    return render(request, 'evenements/evenement_detail.html', context)