from django.db import models

# Create your models here.
class Video(models.Model):

    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    descripcion = models.TextField(null=True,verbose_name='Descripcion')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Portada')
    anio = models.IntegerField(null=True,verbose_name='Año')


    def __str__(self) -> str:
        return self.nombre

    
    def delete(self,using=None,keep_parents=False):
        self.imagen.storage.delete(self.imagen.name) #borrado fisico
        super().delete()
