"""
URL configuration for plateforme_location project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('biens/', include('biens.urls')),
    path('reservations/', include('reservations.urls')),
    path('paiements/', include('paiements.urls')),
    path('avis/', include('avis.urls')),
    path('', include('users.urls')), 
    path('profile_utilisateur/', include('profile_utilisateur.urls')),
    
]
