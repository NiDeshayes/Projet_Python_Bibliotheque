from django.db import models
from django.utils import timezone
from django import forms

class Membre(models.Model):
    nom = models.CharField(max_length=100, default='Nom Inconnu')

    def __str__(self):
        return self.nom

    def mettre_a_jour(self, nouveau_nom):
        self.nom = nouveau_nom
        self.save()

    def supprimer(self):
        self.delete()


class Emprunteur(models.Model):
    nom = models.CharField(max_length=100, default='Nom Inconnu')
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.nom


class Media(models.Model):
    nom = models.CharField(max_length=100, default='Titre Inconnu')
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey('Emprunteur', on_delete=models.SET_NULL, null=True, blank=True)

    def supprimer(self):
        self.delete()

    class Meta:
        abstract = True


class Livre(Media):
    auteur = models.CharField(max_length=100, default='Auteur Inconnu')

    def __str__(self):
        return f"Livre: {self.nom} par {self.auteur}"


class DVD(Media):
    realisateur = models.CharField(max_length=100, default='Réalisateur Inconnu')

    def __str__(self):
        return f"DVD: {self.nom} par {self.realisateur}"


class CD(Media):
    artiste = models.CharField(max_length=100, default='Artiste Inconnu')

    def __str__(self):
        return f"CD: {self.nom} par {self.artiste}"


class JeuDePlateau(models.Model):
    nom = models.CharField(max_length=100, default='Nom Inconnu')
    createur = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Jeu de Plateau: {self.nom}"


class Emprunt(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE, default=1)  # Assurez-vous qu'un membre avec cet ID existe
    livre_emprunte = models.ForeignKey('Livre', on_delete=models.CASCADE, null=True, blank=True)
    dvd_emprunte = models.ForeignKey('DVD', on_delete=models.CASCADE, null=True, blank=True)
    cd_emprunte = models.ForeignKey('CD', on_delete=models.CASCADE, null=True, blank=True)
    date_emprunt = models.DateTimeField(default=timezone.now)
    date_retour = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return (
            f"{self.membre} - "
            f"{self.livre_emprunte or 'Aucun livre'} - "
            f"{self.dvd_emprunte or 'Aucun DVD'} - "
            f"{self.cd_emprunte or 'Aucun CD'} - "
            f"Emprunté le: {self.date_emprunt} - "
            f"Retour prévu: {self.date_retour or 'Non spécifié'}"
        )
