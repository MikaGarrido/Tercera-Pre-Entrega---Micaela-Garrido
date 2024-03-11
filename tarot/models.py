from django.db import models
import datetime
# Create your models here.

class ServicioTarot(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.nombre}'
    class Meta:
        verbose_name = "Servicio Tarot"
        verbose_name_plural = "Servicios Tarot"
    class Meta:
        ordering = ["nombre"]



class Pregunta(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.pregunta}'
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.nombre
