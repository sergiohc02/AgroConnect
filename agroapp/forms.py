# core/forms.py
from django import forms
from .models import RegistroNacimiento

class RegistroNacimientoForm(forms.ModelForm):
    class Meta:
        model = RegistroNacimiento
        fields = ['id_animal', 'fecha_nacimiento', 'hora', 'nombre', 'numero', 'peso', 'raza', 'capa']
