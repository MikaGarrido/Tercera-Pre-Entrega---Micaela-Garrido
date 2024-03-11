from django import forms
import datetime

class ServicioForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    descripcion = forms.CharField(max_length=150, required=True)

class PreguntaForm(forms.Form):
    pregunta = forms.CharField(max_length=255, required=True)
    respuesta = forms.CharField(max_length=300, required=True)

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=datetime.date.today, required=True)
