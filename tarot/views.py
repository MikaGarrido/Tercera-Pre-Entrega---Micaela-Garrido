from django.shortcuts import render

from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")

def serviciotarot(request):
    servicios = ServicioTarot.objects.all()
    return render(request, 'aplicacion/serviciotarot.html', {'servicios': servicios})


def pregunta(request):
    preguntas = Pregunta.objects.all()
    return render(request, 'aplicacion/pregunta.html', {'pregunta': preguntas})

def cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'aplicacion/cliente.html', {'cliente': clientes})

    

#------------------------Forms
def servicioForm(request):
    if request.method == "POST":
        miForm = ServicioForm(request.POST)
        if miForm.is_valid():
            servicio_nombre = miForm.cleaned_data.get("nombre")
            servicio_descripcion = miForm.cleaned_data.get("descripcion")
            serviciotarot = ServicioTarot(nombre=servicio_nombre, descripcion=servicio_descripcion)
            serviciotarot.save()
            return render(request, 'aplicacion/index.html')
    else:
        miForm = ServicioForm()

    return render(request, "aplicacion/servicioForm.html", {"form":miForm} )

def preguntaForm(request):
    if request.method == "POST":
        miForm = PreguntaForm(request.POST)
        if miForm.is_valid():
            preg_pregunta = miForm.cleaned_data.get("pregunta")
            preg_respuesta = miForm.cleaned_data.get("respuesta")
            pregunta = Pregunta(pregunta=preg_pregunta, respuesta=preg_respuesta)
            pregunta.save()
            return render(request, 'aplicacion/index.html')
    else:
        miForm = PreguntaForm()

    return render(request, "aplicacion/preguntaForm.html", {"form":miForm} )

def clienteForm(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_email = miForm.cleaned_data.get("email")
            cliente_fechan = miForm.cleaned_data.get("fecha_nacimiento")
            cliente = Cliente(nombre=cliente_nombre, email=cliente_email, fecha_nacimiento=cliente_fechan)
            cliente.save()
            return render(request, 'aplicacion/index.html')
    else:
        miForm = ClienteForm()

    return render(request, "aplicacion/clienteForm.html", {"form":miForm} )

def buscarServicios(request):
    return render(request, "aplicacion/buscar.html")

def encontrarServicios(request):
    patron = request.GET.get("buscar")
    if patron:
        servicios = ServicioTarot.objects.filter(nombre__icontains=patron)
    else:
        servicios = ServicioTarot.objects.all()

    contexto = {"servicios": servicios}
    return render(request, "aplicacion/serviciotarot.html", contexto)
