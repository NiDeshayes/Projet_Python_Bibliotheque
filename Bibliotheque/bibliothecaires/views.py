import logging
from datetime import datetime, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.urls import reverse
from .models import Membre, Livre, DVD, CD, JeuDePlateau, Emprunt
from .forms import Creationmembre

logger = logging.getLogger('app_mediatheque')

def custom_logout(request):
    logout(request)
    return render(request, 'logout.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('liste_emprunts')
        else:
            error_message = 'Identifiants incorrects'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def supprimer_membre(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    membre.delete()  # Utilisation de la méthode delete() directement
    return redirect('liste_membres')

def liste_medias(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(request, 'liste_medias.html', {'livres': livres, 'dvds': dvds, 'cds': cds, 'jeux': jeux})

def supprimer_media(request, media_id):
    media = get_object_or_404(Media, pk=media_id)
    media.delete()  # Utilisation de la méthode delete() directement
    return redirect('liste_medias')

def liste_emprunts(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'liste_emprunts.html', {'emprunts': emprunts})

def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, 'liste_membres.html', {'membres': membres})


def ajout_membre(request):
    if request.method == 'POST':
        creationmembre = Creationmembre(request.POST)
        if creationmembre.is_valid():
            creationmembre.save()  # Sauvegarde directement à partir du formulaire
            return redirect('liste_membres')
    else:
        creationmembre = Creationmembre()
    return render(request, 'ajoutmembre.html', {'creationmembre': creationmembre})



def liste_livres(request):
    livres = Livre.objects.all()
    return render(request, 'livre.html', {'livres': livres})

def supprimer_livre(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    livre.delete()  # Utilisation de la méthode delete() directement
    return redirect('liste_livres')

def liste_cds(request):
    cds = CD.objects.all()
    return render(request, 'cd.html', {'cds': cds})

def supprimer_cd(request, cd_id):
    cd = get_object_or_404(CD, pk=cd_id)
    cd.delete()  # Utilisation de la méthode delete() directement
    return redirect('liste_cds')

def liste_dvds(request):
    dvds = DVD.objects.all()
    return render(request, 'dvd.html', {'dvds': dvds})

def supprimer_dvd(request, dvd_id):
    dvd = get_object_or_404(DVD, pk=dvd_id)
    dvd.delete()  # Utilisation de la méthode delete() directement
    return redirect('liste_dvds')

def liste_jeux(request):
    jeux = JeuDePlateau.objects.all()
    return render(request, 'jeudeplateau.html', {'jeux': jeux})

def supprimer_jeu(request, jeu_id):
    jeu = get_object_or_404(JeuDePlateau, pk=jeu_id)
    jeu.delete()  # Utilisation de la méthode delete() directement
    return redirect('liste_jeux')

def ajouter_livre(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        auteur = request.POST.get('auteur')
        Livre.objects.create(nom=nom, auteur=auteur)
        return redirect('liste_livres')
    return render(request, 'ajouter_livre.html')

def ajouter_dvd(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        realisateur = request.POST.get('realisateur')
        DVD.objects.create(nom=nom, realisateur=realisateur)
        return redirect('liste_dvds')
    return render(request, 'ajouter_dvd.html')

def ajouter_cd(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        artiste = request.POST.get('artiste')
        CD.objects.create(nom=nom, artiste=artiste)
        return redirect('liste_cds')
    return render(request, 'ajouter_cd.html')

def ajouter_jeu_de_plateau(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        createur = request.POST.get('createur')
        JeuDePlateau.objects.create(nom=nom, createur=createur)
        return redirect('liste_jeux')
    return render(request, 'ajouter_jeu_de_plateau.html')

def mettre_a_jour_membre(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    if request.method == 'POST':
        nouveau_nom = request.POST.get('nouveau_nom')
        membre.nom = nouveau_nom
        membre.save()
        return redirect('liste_membres')
    return render(request, 'mettre_a_jour_membre.html', {'membre': membre})

def confirmation_emprunt(request):
    return render(request, 'confirmation_emprunt.html')

def limite_emprunts(request):
    return render(request, 'limite_emprunts.html')

def emprunts_en_retard(request):
    emprunts = Emprunt.objects.filter(date_retour__lt=timezone.now())
    return render(request, 'page_des_emprunts_en_retard.html', {'emprunts': emprunts})

def emprunter_media(request, media_type, media_id):
    if request.method == 'POST':
        membre_id = request.POST.get('membre_id')
        membre = get_object_or_404(Membre, pk=membre_id)

        emprunts_actifs = Emprunt.objects.filter(membre_id=membre_id).count()
        if emprunts_actifs >= 3:
            return redirect('limite_emprunts')

        emprunts_en_retard = Emprunt.objects.filter(membre=membre, date_retour__lt=datetime.now())
        if emprunts_en_retard.exists():
            return redirect('emprunts_en_retard')

        if media_type == 'livre':
            media = get_object_or_404(Livre, pk=media_id)
        elif media_type == 'dvd':
            media = get_object_or_404(DVD, pk=media_id)
        elif media_type == 'cd':
            media = get_object_or_404(CD, pk=media_id)
        else:
            return HttpResponseBadRequest("Type de média non valide.")

        if not media.disponible:
            logger.warning(f'Média non disponible {media.id} car emprunté par {membre_id}')
            return HttpResponseBadRequest("Ce média n'est pas disponible.")

        date_retour = timezone.now() + timedelta(days=7)
        
        if media_type == 'livre':
            Emprunt.objects.create(membre=membre, livre_emprunte=media, date_emprunt=timezone.now(), date_retour=date_retour)
        elif media_type == 'dvd':
            Emprunt.objects.create(membre=membre, dvd_emprunte=media, date_emprunt=timezone.now(), date_retour=date_retour)
        elif media_type == 'cd':
            Emprunt.objects.create(membre=membre, cd_emprunte=media, date_emprunt=timezone.now(), date_retour=date_retour)

        logger.info(f'Média {media.id} emprunté par {membre_id}')
        return redirect('confirmation_emprunt')

    else:
        membres = Membre.objects.all()
        if media_type == 'livre':
            media = Livre.objects.all()
        elif media_type == 'dvd':
            media = DVD.objects.all()
        elif media_type == 'cd':
            media = CD.objects.all()
        else:
            media = []

        return render(request, 'emprunter_media.html', {'membres': membres, 'media': media})
