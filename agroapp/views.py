from django.shortcuts import render

# Create your views here.

def registrar_nacimiento(request):
    return render(request, 'registrar_nacimiento.html')

def registrar_muerte(request):
    return render(request, 'registrar_muerte.html')

def registrar_enfermedad(request):
    return render(request, 'registrar_enfermedad.html')

def registrar_lote_cubricion(request):
    return render(request, 'registrar_lote_cubricion.html')
