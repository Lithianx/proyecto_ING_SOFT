"""
URL configuration for sitio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from aplicacion.views import *

urlpatterns = [
    path('', index, name='index'),
    path('contacto/', contacto, name='contacto'),
    path('eventos/', eventos, name='eventos'),
    path('reserva/', reserva, name='reserva'),
    path('servicios/', servicios, name='servicios'),
    path('administracion/', administracion, name='administracion'),
    path('registrarse/', registrarse, name='registrarse'),
    path('reserva_exitosa/', reserva_exitosa, name='reserva_exitosa'),
    path('eliminar_reserva/<int:id>/', eliminar_reserva, name='eliminar_reserva'),
    path('confirmar_eliminar_reserva/<int:id>/', confirmar_eliminar_reserva, name='confirmar_eliminar_reserva'),
    path('editar_reserva/<int:id>/', editar_reserva, name='editar_reserva'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),

]


#urls de la aplicacion