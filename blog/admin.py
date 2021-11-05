from django.contrib import admin
from .models import Post  # ici on importe notre objet ou model (le blog (ou Post)) qu'on a modeliser

# Register your models here.

admin.site.register(Post)  #permet denregistrer notre objet ou model
