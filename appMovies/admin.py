from django.contrib import admin
from appMovies.models import Genero,Peliculas
# Register your models here.

#  Esto me permite visualizar en el administrador de Django los modelos generados 
# para su administración.
admin.site.register(Genero)
admin.site.register(Peliculas)