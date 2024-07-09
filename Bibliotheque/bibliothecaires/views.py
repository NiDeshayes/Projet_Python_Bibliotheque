from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Livre, DVD, CD, JeuDePlateau, Membre
from django.contrib.auth.models import User

@login_required
def ajouter_membre(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        membre = Membre.objects.create(user=user)
        return redirect('liste_membres')
    return render(request, 'bibliothecaires/ajouter_membre.html')

@login_required
def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, 'bibliothecaires/liste_membres.html', {'membres': membres})

@login_required
def mettre_a_jour_membre(request, membre_id):
    membre = get_object_or_404(Membre, id=membre_id)
    if request.method == 'POST':
        membre.user.username = request.POST['username']
        membre.user.set_password(request.POST['password'])
        membre.user.save()
        membre.save()
        return redirect('liste_membres')
    return render(request, 'bibliothecaires/mettre_a_jour_membre.html', {'membre': membre})

@login_required
def supprimer_membre(request, membre_id):
    membre = get_object_or_404(Membre, id=membre_id)
    membre.user.delete()
    membre.delete()
    return redirect('liste_membres')

@login_required
def liste_medias(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(request, 'bibliothecaires/liste_medias.html', {'livres': livres, 'dvds': dvds, 'cds': cds, 'jeux': jeux})

@login_required
def emprunter_media(request, media_type, media_id):
    media = get_object_or_404(eval(media_type.capitalize()), id=media_id)
    if media.disponible:
        media.disponible = False
        media.emprunteur = request.user
        media.save()
    return redirect('liste_medias')

@login_required
def rendre_media(request, media_type, media_id):
    media = get_object_or_404(eval(media_type.capitalize()), id=media_id)
    if media.emprunteur == request.user:
        media.disponible = True
        media.emprunteur = None
        media.save()
    return redirect('liste_medias')
