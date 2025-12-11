from django.urls import path
from . import views

app_name = 'programmes'

urlpatterns = [
    path('', views.liste_programmes, name='liste'),
    path('<int:pk>/', views.detail_programme, name='detail'),
]
