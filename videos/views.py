from django.http import HttpResponse
from django.shortcuts import redirect, render

from videos.forms import VideoForm
from videos.models import Video

# Create your views here.
def index(request):
    # return HttpResponse('<h1>hola mundo  django 😎</h1>')
    return render(request,'videos/index.html',{'titulo':'OTRO TITULO','variable':-2})


def quienes_somos(request):
    return render(request,'videos/quienes_somos.html')

def listado(request):
    # IR A BUSCAR A LA BASE y RENDERIZAR PELICULAS
    peliculas = Video.objects.all
    return render(request,'videos/listado.html',{'peliculas':peliculas})

def crear(request):
    formulario = VideoForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('listado_video')
    return render(request,'videos/crear.html',{'formulario':formulario})


def editar(request):
    return render(request,'videos/editar.html')

def eliminar(request,id_video):
    video = Video.objects.get(id=id_video)
    video.delete()
    return redirect('listado_video')