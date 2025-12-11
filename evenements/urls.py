from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_evenements, name='evenements'),
]