from django.urls import path, include
from .views import *
from .forms import *

urlpatterns = [
    path('', home, name="home"),
    path('cliente/', cliente, name="cliente"),
    path('pregunta/',pregunta, name="pregunta"),
    path('serviciotarot/', serviciotarot, name="serviciotarot"),

    path('servicio_form/', servicioForm, name="servicio_form"),
    path('pregunta_form/', preguntaForm, name="pregunta_form"),
    path('cliente_form/', clienteForm, name="cliente_form"),

    path('buscar_servicios/', buscarServicios, name="buscar_servicios"),
    path('encontrar_servicios/', encontrarServicios, name="encontrar_servicios"),
]    