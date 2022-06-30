from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.index,name='inicio'),
    path('quienes_somos/', views.quienes_somos,name='quienes_somos'),
    path('listado/', views.listado,name='listado_pelicula'),
    path('crear/', views.crear,name='crear_pelicula'),
    path('editar/', views.editar,name='editar_pelicula'),
    path('eliminar/', views.eliminar,name='eliminar_pelicula'),

]


