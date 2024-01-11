from django.shortcuts import render, redirect
from .models import RegistroNacimiento
from .forms import RegistroNacimientoForm

def registrar_nacimiento(request):
    if request.method == 'POST':
        form = RegistroNacimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('página_de_exito')  # Puedes redirigir a una página de éxito o a donde desees
    else:
        form = RegistroNacimientoForm()

    return render(request, 'registrar_nacimiento.html', {'form': form})

def registrar_muerte(request):
    return render(request, 'registrar_muerte.html')

def registrar_enfermedad(request):
    return render(request, 'registrar_enfermedad.html')

def registrar_lote_cubricion(request): 
    return render(request, 'registrar_lote_cubricion.html')
