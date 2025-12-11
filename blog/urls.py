from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_articles, name='blog'),
    path('<slug:slug>/', views.detail_article, name='detail_article'),
]