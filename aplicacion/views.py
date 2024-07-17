from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from aplicacion.forms import *


def base(request):
    return render(request,'aplicacion/base.html')

def index(request):
    return render(request,'aplicacion/index.html')

def buscar_reserva(request):
    return render(request, 'aplicacion/buscar_reserva.html')

def consultar_reserva(request):
    return render(request, 'aplicacion/consultar_reserva.html')

def contacto(request):
    return render(request, 'aplicacion/contacto.html')

def detalle_reserva(request):
    return render(request, 'aplicacion/detalle_reserva.html')

def eliminar_reserva(request):
    return render(request, 'aplicacion/eliminar_reserva.html')

def eventos(request):
    return render(request, 'aplicacion/eventos.html')

def gestion_reservas(request):
    return render(request, 'aplicacion/gestion_reservas.html')

def modificar_reserva(request):
    return render(request, 'aplicacion/modificar_reserva.html')

@login_required
def reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.user = request.user
            reserva.save()
            return redirect('reserva_exitosa')
    else:
        form = ReservaForm()
    return render(request, 'aplicacion/reserva.html', {'form': form})

@login_required
def reserva_exitosa(request):
    return render(request, 'aplicacion/reserva_exitosa.html')

def servicios(request):
    return render(request, 'aplicacion/servicios.html')

def administracion(request):
    reservas = Reserva.objects.all()
    return render(request, 'aplicacion/administracion.html', {'reservas': reservas})

def confirmar_eliminar_reserva(request):
    return render(request, 'aplicacion/confirmar_eliminar_reserva.html')

def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        reserva.delete()
        return redirect('administracion')
    
    return render(request, 'aplicacion/confirmar_eliminar_reserva.html', {'obj': reserva})


def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('administracion')  
    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'aplicacion/editar_reserva.html', {'form': form, 'reserva': reserva})

    


def form_inicio_sesion(request):
    if request.method == 'POST':
        form = form_login(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = form_login()
    return render(request, 'login.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('index')


def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            nombre = form.cleaned_data.get('nombre')
            telefono = form.cleaned_data.get('telefono')
            direccion = form.cleaned_data.get('direccion')
            
            # Creando el cliente asociado al usuario
            cliente = Cliente.objects.create(
                user=user,
                nombre=nombre,
                email=email,
                telefono=telefono,
                direccion=direccion
            )
            cliente.save()
            
            # Autenticación y login del usuario
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirigir a la página de inicio después del registro
    else:
        form = RegistroForm()

    return render(request, 'aplicacion/registrarse.html', {'form': form})

















