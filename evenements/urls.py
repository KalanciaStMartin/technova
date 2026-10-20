from django.urls import path
from . import views

urlpatterns = [
    # ... tes autres URLs existantes (accueil, etc.)

    path('', views.evenements_liste, name='evenements'),
    path('<int:pk>/', views.evenement_detail, name='evenement_detail'),
]