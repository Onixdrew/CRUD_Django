from django.shortcuts import render
from django.db import Error
from appMovies.models import Genero, Peliculas
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

# ////////////////////////////// Generos

def vistaAgregarGenero(request):
    return render(request, "agregarGenero.html")


@csrf_exempt
def agregarGenero(request):
    
    try:
        nombre:request.POST['newGenero']
        
        # se crea un objeto de tipo genero
        genero=Genero(genNombre=nombre)
        genero.save()
        mensaje='Genero agregado correctamente'
        
    except Error as error:
        mensaje=str(error)
    
    retorno={"mensaje":mensaje}
    
    return render(retorno, 'agregarGenero',retorno )


# ////////////////////////////////// Peliculas


def listarPeliculas(request):
    peliculas= Peliculas.objects.all()
    retorno= {"peliculas": list(peliculas)}
    
    return render(request, 'listarPeliculas.html',retorno )



def vistaAgregarPeliculas(request):
    generos= Genero.objects.all()
    retorno= {"generos": generos}
    return render(request, "agregarPeliculas.html", retorno)



@csrf_exempt
def agregarPelicula(request):
    try:
        codigoCall = request.POST['codigo']
        tituloCall = request.POST['titulo']
        protagonista = request.POST['protagonista']
        duracionCall = int(request.POST['duracion'])
        resumenCall = request.POST['resumen']
        fotoCall = request.FILES['foto']
        idGenero = int(request.POST['pelGenero'])
        
        genero = Genero.objects.get(pk=idGenero)
        
        # crear objeto pelicula}
        
        pelicula=Peliculas(codigo=codigoCall,
                           titulo=tituloCall,
                           protagonista=protagonista,
                           duracion=duracionCall,
                           resumen=resumenCall,
                           foto=fotoCall,
                           pelGenero=genero)
        
        pelicula.save()
        mensaje="Pelicula agregada correctamente"
        
    except Error as error:
        mensaje=str(error)
        
    retorno={"mensaje":mensaje, "idPelicula":pelicula.id}
    return JsonResponse(retorno)
