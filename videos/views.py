from django.http import HttpResponse
from django.shortcuts import redirect, render

from videos.forms import VideoForm

# Create your views here.
def index(request):
    # return HttpResponse('<h1>hola mundo  django 😎</h1>')
    return render(request,'videos/index.html',{'titulo':'OTRO TITULO','variable':-2})


def quienes_somos(request):
    return render(request,'videos/quienes_somos.html')

def listado(request):
    # IR A BUSCAR A LA BASE y RENDERIZAR PELICULAS
    peliculas = [
        {
            'id':1,
            'nombre':'El senor de los anillos 1',
            'descripcion':'2000 +13 180m',
            'imagen':'imagen.jpg',

        },
        {
            'id':2,
            'nombre':'harry potter',
            'descripcion':'2000 +13 180m',
            'imagen':'imagen.jpg',

        },
        {
            'id':3,
            'nombre':'Toy Story 3',
            'descripcion':'2000 +13 180m',
            'imagen':'imagen.jpg',
        },
        {
            'id':4,
            'nombre':'Toy Story 1',
            'descripcion':'2000 +13 180m',
            'imagen':'imagen.jpg',
        }

    ]
    return render(request,'videos/listado.html',{'peliculas':peliculas})

def crear(request):
    formulario = VideoForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('listado_pelicula')
    return render(request,'videos/crear.html',{'formulario':formulario})


def editar(request):
    return render(request,'videos/editar.html')

def eliminar(request):
    pass