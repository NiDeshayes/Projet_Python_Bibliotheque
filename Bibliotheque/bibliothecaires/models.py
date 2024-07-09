# bibliothecaires/models.py
from django.db import models
from django.contrib.auth.models import User

class Media(models.Model):
    name = models.CharField(max_length=100)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True

class Livre(Media):
    auteur = models.CharField(max_length=100)

class DVD(Media):
    realisateur = models.CharField(max_length=100)

class CD(Media):
    artiste = models.CharField(max_length=100)

class JeuDePlateau(models.Model):
    name = models.CharField(max_length=100)
    createur = models.CharField(max_length=100)

class Membre(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bloque = models.BooleanField(default=False)
