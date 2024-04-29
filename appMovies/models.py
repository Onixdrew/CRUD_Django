from django.db import models

# Create your models here.

class Genero(models.Model):
    genNombre=models.CharField(max_length=50, unique=True)
    
    # Esta funcion devuelve el un string(nombre) para poder visualizarlo en el admin
    def __str__(self) -> str:
        return self.genNombre
    


class Peliculas(models.Model):
    codigo=models.CharField(max_length=9)
    titulo=models.CharField(max_length=50)
    protagonista=models.CharField(max_length=50)
    duracion=models.IntegerField()
    resumen=models.CharField(max_length=2000)
    foto=models.ImageField(upload_to=f'fotos/', null=True, blank=True)
    pelGenero=models.ForeignKey(Genero, on_delete=models.PROTECT)
    
    
    def __str__(self) -> str:
        return self.titulo



