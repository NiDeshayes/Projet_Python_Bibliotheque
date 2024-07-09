from django.urls import path
from . import views

urlpatterns = [
    path('liste_medias/', views.liste_medias, name='liste_medias'),
]
