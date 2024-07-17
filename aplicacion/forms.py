from django import forms
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from aplicacion.models import *




class form_login(AuthenticationForm):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)




class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nombre = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nombre', 'telefono', 'direccion']





class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class ReservaForm(forms.ModelForm):
    fecha_inicio = forms.DateTimeField(widget=DateTimeInput(attrs={'class': 'form-control'}))
    fecha_fin = forms.DateTimeField(widget=DateTimeInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Reserva
        fields = [
            'hotel',
            'tipo_evento',
            'descripcion',
            'fecha_inicio',
            'fecha_fin',
        ]

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get("fecha_inicio")
        fecha_fin = cleaned_data.get("fecha_fin")

        if fecha_inicio and fecha_fin:
            if fecha_fin <= fecha_inicio:
                raise forms.ValidationError("La fecha de fin debe ser posterior a la fecha de inicio.")

        return cleaned_data





# class ReservaForm(forms.ModelForm):
#     fecha_inicio = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
#     fecha_fin = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))

#     class Meta:
#         model = Reserva
#         fields = [
#             'hotel',
#             'tipo_evento',
#             'descripcion',
#             'fecha_inicio',
#             'fecha_fin',
#         ]

#     def clean(self):
#         cleaned_data = super().clean()
#         fecha_inicio = cleaned_data.get("fecha_inicio")
#         fecha_fin = cleaned_data.get("fecha_fin")

#         if fecha_inicio and fecha_fin:
#             if fecha_fin <= fecha_inicio:
#                 raise forms.ValidationError("La fecha de fin debe ser posterior a la fecha de inicio.")

#         return cleaned_data
# class ReservaForm(forms.ModelForm):
#     class Meta:
#         model = Reserva
#         fields = [
#             'hotel', 
#             'tipo_evento', 
#             'descripcion', 
#             'fecha_inicio', 
#             'fecha_fin', 
            
#         ]

#     def clean(self):
#         cleaned_data = super().clean()
#         fecha_inicio = cleaned_data.get("fecha_inicio")
#         fecha_fin = cleaned_data.get("fecha_fin")

#         if fecha_inicio and fecha_fin:
#             if fecha_fin <= fecha_inicio:
#                 raise forms.ValidationError("La fecha de fin debe ser posterior a la fecha de inicio.")

#         return cleaned_data