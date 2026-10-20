from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('inscription/success/', views.inscription_success, name='inscription_success'),
]