from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_programmes, name='liste_programmes'),
    path('<int:pk>/', views.detail_programme, name='detail_programme'),
]