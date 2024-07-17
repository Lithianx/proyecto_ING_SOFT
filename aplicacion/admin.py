from django.contrib import admin
from .models import *

class HotelAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'descripcion')
    search_fields = ('nombre', 'ubicacion')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'direccion')
    search_fields = ('nombre', 'email')

class EventoAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'cliente', 'tipo_evento', 'descripcion', 'fecha_inicio', 'fecha_fin')
    search_fields = ('hotel__nombre', 'cliente__nombre', 'tipo_evento', 'descripcion')
    list_filter = ('hotel', 'tipo_evento', 'fecha_inicio')

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'tipo_evento', 'descripcion', 'fecha_inicio', 'fecha_fin')
    search_fields = ('user__username', 'hotel__nombre', 'tipo_evento', 'descripcion')
    list_filter = ('hotel', 'tipo_evento', 'fecha_inicio')

admin.site.register(Hotel, HotelAdmin)
# admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Reserva, ReservaAdmin)



  