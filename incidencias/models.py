from django.db import models
from core.models import Incidencia  # Usamos el modelo existente del core

# No es necesario redefinir el modelo Incidencia aquí ya que lo estamos importando de core.models

class ImagenIncidencia(models.Model):
    incidencia = models.ForeignKey(Incidencia, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='incidencias/')
    creado_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Imagen de Incidencia"
        verbose_name_plural = "Imágenes de Incidencias"
        ordering = ['-creado_el']

    def __str__(self):
        return f"Imagen {self.id} de {self.incidencia.titulo}"
    incidencia = models.ForeignKey(
        Incidencia, 
        on_delete=models.CASCADE,
        related_name='imagenes'
    )
    imagen = models.ImageField(upload_to='incidencias/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    es_resolucion = models.BooleanField(
        default=False,
        help_text="Indica si esta imagen es de la resolución de la incidencia"
    )

    class Meta:
        verbose_name = "Imagen de Incidencia"
        verbose_name_plural = "Imágenes de Incidencias"
