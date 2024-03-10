from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('cliente/', cliente, name="cliente"),
    path('pregunta/',pregunta, name="pregunta"),
    path('serviciotarot/', serviciotarot, name="serviciotarot"),
]