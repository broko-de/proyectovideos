from django.http import HttpResponse, JsonResponse
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


def editar(request,id_video):
    try:
        video = Video.objects.get(id=id_video)
    except Video.DoesNotExist:
        return render(request,'videos/404.html')
    formulario = VideoForm(request.POST or None,request.FILES or None,instance=video)
    if formulario.is_valid():
        formulario.save()
        return redirect('listado_video')
    return render(request,'videos/editar.html',{'formulario':formulario})

def eliminar(request,id_video):
    video = Video.objects.get(id=id_video)
    video.delete()
    return redirect('listado_video')

def listado_json(request):
    videos = Video.objects.all().values()
    videos_list = list(videos)
    response = {'status':'Ok','code':200,'message':'Listado de videos','data':videos_list}
    return JsonResponse(response,safe=False)