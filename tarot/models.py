from django.db import models

# Create your models here.

class ServicioTarot(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
