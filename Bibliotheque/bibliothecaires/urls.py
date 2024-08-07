from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [


    path('', views.custom_login, name='login'),
    path('iste_emprunts/', views.liste_emprunts, name='liste_emprunts'),
    path('logout/',views.custom_logout, name='logout'),
    path('membres/', views.liste_membres, name='liste_membres'),
    path('ajoutmembre/', views.ajout_membre, name='ajoutmembre'),
    path('liste_medias/', views.liste_medias, name='liste_medias'),
    path('ajouter-livre/', views.ajouter_livre, name='ajouter_livre'),
    path('ajouter-dvd/', views.ajouter_dvd, name='ajouter_dvd'),
    path('ajouter-cd/', views.ajouter_cd, name='ajouter_cd'),
    path('ajouter-jeu-de-plateau/', views.ajouter_jeu_de_plateau, name='ajouter_jeu_de_plateau'),
    path('liste_livres/', views.liste_livres, name='liste_livres'),
    path('supprimer_livre/<int:livre_id>/', views.supprimer_livre, name='supprimer_livre'),
    path('liste_dvds/', views.liste_dvds, name='liste_dvds'),
    path('supprimer_dvd/<int:dvd_id>/', views.supprimer_dvd, name='supprimer_dvd'),
    path('liste_jeux/', views.liste_jeux, name='liste_jeux'),
    path('supprimer_jeu/<int:jeu_id>/', views.supprimer_jeu, name='supprimer_jeu'),
    path('liste_cds/', views.liste_cds, name='liste_cds'),
    path('supprimer_cd/<int:cd_id>/', views.supprimer_cd, name='supprimer_cd'),
    path('emprunter_media/<str:media_type>/<int:media_id>/', views.emprunter_media, name='emprunter_media'),
    path('confirmation_emprunt/', views.confirmation_emprunt, name='confirmation_emprunt'),
    path('limite_emprunts/', views.limite_emprunts, name='limite_emprunts'),
    path('emprunts_en_retard/', views.emprunts_en_retard, name='emprunts_en_retard'),
    path('mettre-a-jour-membre/<int:membre_id>/', views.mettre_a_jour_membre, name='mettre_a_jour_membre'),
    path('supprimer_membre/<int:membre_id>/', views.supprimer_membre, name='supprimer_membre'),
]
