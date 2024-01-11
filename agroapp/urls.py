# core/urls.py
from django.urls import path
from .views import (
    registrar_nacimiento,
    registrar_muerte,
    registrar_enfermedad,
    registrar_lote_cubricion,
)

urlpatterns = [
    path('registrar-nacimiento/', registrar_nacimiento, name='registrar_nacimiento'),
    path('registrar-muerte/', registrar_muerte, name='registrar_muerte'),
    path('registrar-enfermedad/', registrar_enfermedad, name='registrar_enfermedad'),
    path('registrar-lote-cubricion/', registrar_lote_cubricion, name='registrar_lote_cubricion'),
]
