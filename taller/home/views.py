from django.shortcuts import render, HttpResponse
from .models import Persona
from .forms import CreaPersonaForm

def home(request):
    return render(request, 'home/index.html')

def pagina_uno(request):
    personas = Persona.objects.all()
    paco = Persona.objects.get(nombre="Paco")
    m_o = Persona.objects.filter(apellidos="Martinez Orotava")
    return render(request, 'home/pagina_uno.html',  {"personas":personas, "paco":paco, "mo":m_o})

def pagina_dos(request):
    formulario = CreaPersonaForm()

    if request.method == "POST":
        formulario = CreaPersonaForm(request.POST)
        if formulario.is_valid():
            registro = formulario.save(commit=False)
            registro.save()
            return render(request, 'home/pagina_dos.html', {"ok":"Se ha registrado correctamente"})
        else:
            formulario = CreaPersonaForm()
            return render(request, 'home/pagina_dos.html', {"error":"Hubo un problema con el formulario"})

    return render(request, 'home/pagina_dos.html', {"formulario":formulario})