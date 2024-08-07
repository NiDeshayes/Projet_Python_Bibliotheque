from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bibliothecaires.urls')),
    path('emprunteur/', include('membres.urls')),
    
]