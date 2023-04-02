from django.db import models

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='Imagenes/',verbose_name='imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripcion', null=True)
    def __str__(self):
        fila = "Titulo: " + self.titulo + " Descripcion: " + self.descripcion
        return fila
