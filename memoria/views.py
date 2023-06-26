from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.urls import reverse_lazy
from .models import Memorial, Planes
import requests
from .forms import formUserRegistro, CustomChangePasswordForm, CustomChangePasswordForma




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

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Contraseña incorrecta')
            return render(request, 'memoria/userLogin.html')
    else:
        return render(request, 'memoria/userLogin.html')

    
def userLogout(request):
    logout(request)
    return redirect("userLogin")   

    
@login_required
def dashboard(request):
    return render(request, 'memoria/dashboard_home.html')

def userRegistro(request):
    if request.method == 'POST':
        form = formUserRegistro(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            group = Group.objects.get(name='Clientes')  
            user.groups.add(group)
            
            activation_link = 'http://localhost:8000/activar-cuenta/' + str(user.id)
            imagen_url = request.build_absolute_uri('https://virtual.cl/img/logo1.png')
            contenido_html = f"""
                <html>
                <head></head>
                <body>
                    <img src="{imagen_url}" style="width:200px"><br>
                    <h2>Bienvenido a MemorIA</h2>
                    <h2>{user.username.upper()}</h2><h3>
                    <a href="{activation_link}">Haz clic aquí para activar tu cuenta</a></h3>
                </body>
                </html>
            """
            send_mail(
                'Activa tu cuenta',
                '',
                'noreply@tu-sitio.com',
                [user.email],
                fail_silently=False,
                html_message=contenido_html
            )
            messages.success(request, 'Registro exitoso. Se ha enviado un correo electrónico para activar tu cuenta.')
            return redirect('dashboard')  
    else:
        form = formUserRegistro()
    return render(request, 'memoria/userRegistro.html', {'userRegistro': form})



User = get_user_model()
def activar_cuenta(request, user_id):
    try:
        user = User.objects.get(id=user_id, is_active=False)
        # Activa la cuenta del usuario
        user.is_active = True
        user.save()
        return render(request, 'memoria/cuenta_activada.html')
    except User.DoesNotExist:
        return render(request, 'memoria/error_activacion.html')
    

class CustomChangePasswordView(PasswordChangeView):
    form_class = CustomChangePasswordForma
    template_name = 'memoria/dashboard_pass.html'
    success_url = reverse_lazy('userLogout')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Contraseña cambiada correctamente.')
        logout(self.request)
        return response
    