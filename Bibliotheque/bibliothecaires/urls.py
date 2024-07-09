from django.urls import path
from . import views

urlpatterns = [
    path('ajouter_membre/', views.ajouter_membre, name='ajouter_membre'),
    path('liste_membres/', views.liste_membres, name='liste_membres'),
    path('mettre_a_jour_membre/<int:membre_id>/', views.mettre_a_jour_membre, name='mettre_a_jour_membre'),
    path('supprimer_membre/<int:membre_id>/', views.supprimer_membre, name='supprimer_membre'),
    path('liste_medias/', views.liste_medias, name='liste_medias'),
    path('emprunter_media/<str:media_type>/<int:media_id>/', views.emprunter_media, name='emprunter_media'),
    path('rendre_media/<str:media_type>/<int:media_id>/', views.rendre_media, name='rendre_media'),
]
