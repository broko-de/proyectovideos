from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='inicio'),
    path('quienes_somos/', views.quienes_somos,name='quienes_somos'),
    path('videos/listado/', views.listado,name='listado_video'),
    path('videos/crear/', views.crear,name='crear_video'),
    path('videos/editar/<int:id_video>', views.editar,name='editar_video'),
    path('videos/eliminar/<int:id_video>', views.eliminar,name='eliminar_video'),
    path('videos/listado_json/', views.listado_json,name='listado_json'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


