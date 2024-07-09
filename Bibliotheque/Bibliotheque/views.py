# bibliotheque/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenue à la médiathèque. Utilisez /bibliothecaires/ pour accéder à l'application des bibliothécaires ou /membres/ pour accéder à l'application des membres.")
