from django.urls import path
from .import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # la premiere partie ou cest vide la cest juste parce que c'est un utilisateur quelconque qui va arriver sur l'url
]

























"""Comme vous pouvez le voir, nous assignons une vue appelée post_list à 
l'URL racine. Ce modèle d’URL correspond à une chaîne 
vide et le résolveur d'URL de Django ignore le nom de domaine 
(par exemple, http://127.0.0.1:8000/), soit la première partie de l'URL.
 Ce pattern va donc indiquer à Django d'afficher la vue views.post_list à
  un utilisateur de votre site web qui se rendrait à l'adresse "http://127.0.0.1:8000/".

"""