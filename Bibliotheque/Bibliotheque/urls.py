from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Vue pour l'URL racine
def home(request):
    return HttpResponse("Bienvenue à la médiathèque!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bibliothecaires/', include('bibliothecaires.urls')),
    path('membres/', include('membres.urls')),
    path('', home),  # Définir l'URL racine
]
