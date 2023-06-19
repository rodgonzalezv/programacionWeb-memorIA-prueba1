from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .models import Memorial, Planes
import requests
from .forms import LoginForm



# Create your views here.
def home(request):
    # Toda la logica que quieran! 
    return render(request, "memoria/home.html")

def quienes_somos(request):
    return render(request, "memoria/quienes_somos.html")

def planes(request):
    listaPlanes=Planes.objects.all()

    url = 'https://mindicador.cl/api'
    response = requests.get(url)
    data = response.json()
    dolar_value = data['dolar']['valor']
    uf_value = data['uf']['valor']
    bitcoin_value = data['bitcoin']['valor']
    context = {
        "planes": listaPlanes,
        "dolar": dolar_value,
        "uf": uf_value,
        "bitcoin": bitcoin_value
    }
    
    
    return render(request, "memoria/planes.html", context)

def galeria(request):
    return render(request, "memoria/galeria.html")

def contacto(request):
    return render(request, "memoria/contacto.html")

def dashboard(request):
    return render(request, "memoria/dashboard.html")

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar_sesion')

def vista_formulario(request):
    formulario = LoginForm()  # Crea una instancia del formulario
    return render(request, 'formulario.html', {'form': formulario})