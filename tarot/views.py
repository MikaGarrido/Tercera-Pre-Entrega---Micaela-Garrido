from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render(request, "aplicacion/index.html")

def serviciotarot(request):
    contexto = {'serviciotarot': ServicioTarot.objects.all()}
    return render(request, "aplicacion/serviciotarot.html")

def pregunta(request):
    return render(request, "aplicacion/pregunta.html")

def cliente(request):
    return render(request, "aplicacion/cliente.html")
