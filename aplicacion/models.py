from django.db import models
from django.contrib.auth.models import User

hoteles = [
    ('Veranum Santiago', 'Veranum Santiago'),
    ('Veranum Valparaiso', 'Veranum Valparaiso'),
]

eventos = [
    ('Boda', 'Boda'),
    ('Seminarios', 'Seminarios'),
    ('Conferencias', 'Conferencias'),
    ('Corporativo', 'Corporativo'),
    ('Talleres', 'Talleres'),
    ('Ocasiones Personales', 'Ocasiones Personales'),
]

regiones = [
    ('Metropolitana', 'Metropolitana'),
    ('IV REGION', 'IV REGION'),
]

class Hotel(models.Model):
    nombre = models.CharField(max_length=200, choices=hoteles)
    ubicacion = models.CharField(max_length=200, choices=regiones)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Evento(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_evento = models.CharField(max_length=200, choices=eventos)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    
    def __str__(self):
        return f'{self.tipo_evento} en {self.hotel.nombre} - Cliente: {self.cliente.nombre}'

class Reserva(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    tipo_evento = models.CharField(max_length=200, choices=eventos)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reserva de {self.user.username} para {self.tipo_evento} en {self.hotel.nombre}'


