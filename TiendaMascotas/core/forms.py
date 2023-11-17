from django import forms
from django.forms import ModelForm, fields, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Categoria, Producto, Bodega, Perfil
from django.forms.widgets import SelectDateWidget

form_hidden = {'class': 'd-none'}
form_select = {'class': 'form-select'}
form_control = {'class': 'form-control'}
form_text_area = {'class': 'form-control', 'rows': '3'}
form_file = {'class': 'form-control-file', 'title': 'Debe subir una imagen'}
form_check = {'class': 'form-check-input'}
form_password = {'class': 'form-control text-danger', 'value': '123'}


class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()


class IngresarForm(Form):
    username = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Username")
    password = forms.CharField(widget=forms.PasswordInput(attrs=form_control), label="Contraseña")
    class Meta:
        fields = ['username', 'password']

class RegistrarForm(UserCreationForm):
    rut = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '18.408.449-K', 'class': 'form-control'}), label="Rut", max_length=15, required=True, )
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'agustin', 'class': 'form-control'}), label="Username", required=True)
    nombre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Agustín', 'class': 'form-control'}), label="Nombre", required=True)
    apellido = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'González', 'class': 'form-control'}), label="Apellido", required=True)
    correo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'agustingonzalezmurua@gmail.com', 'class': 'form-control'}), label="Correo", required=True)
    direccion = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Hierbas Buenas 377', 'class': 'form-control'}), label="Dirección", required=True)
    subscrito = forms.BooleanField(widget=forms.CheckboxInput(attrs=form_check), label='Subscripción', required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '********', 'class': 'form-control'}), label="Contraseña", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '********', 'class': 'form-control'}), label="Confirmar Contraseña", required=True)
    imagen = forms.CharField(widget=forms.FileInput(attrs=form_file), label='Imagen', required=True)

    class Meta:
        model = User
        fields = ['rut', 'username', 'nombre','apellido', 'correo', 'direccion', 'subscrito', 'password1', 'password2', 'imagen']

class MisDatosForm(UserCreationForm):
    rut = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Rut", max_length=15, required=True, )
    username = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Username", required=True)
    nombre = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Nombre", required=True)
    apellido = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Apellido", required=True)
    correo = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Correo", required=True)
    direccion = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Dirección", required=True)
    subscrito = forms.BooleanField(widget=forms.CheckboxInput(attrs=form_check), label='Subscripción', required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), label="Contraseña", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), label="Confirmar Contraseña", required=True)
    imagen = forms.CharField(widget=forms.FileInput(attrs=form_file), label='Imagen', required=True)

    class Meta:
        model = User
        fields = ['rut', 'username', 'nombre','apellido', 'correo', 'direccion', 'subscrito', 'password1', 'password2', 'imagen']
    
class MantenedorProducto(Form):
    id = forms.IntegerField(widget=forms.NumberInput(attrs=form_control), label="ID(Poblar solamente si se desea eliminar o actualizar)", required=False, )
    categoria_choices = Categoria.objects.all().values_list('id', 'nombre')
    categoria = forms.ChoiceField(choices=categoria_choices, widget=forms.Select(attrs={'class': 'form_control'}), label="Categoría", required=False)
    nombre = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Nombre Producto", required=False)
    descripcion = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Descripción", required=False)
    precio = forms.IntegerField(widget=forms.TextInput(attrs=form_control), label="Precio", required=False)
    descuento_subscriptor = forms.IntegerField(widget=forms.TextInput(attrs=form_control), label="Descuento subscriptor", required=False)
    descuento_oferta = forms.IntegerField(widget=forms.TextInput(attrs=form_control), label="Descuento por oferta", required=False)
    imagen = forms.CharField(widget=forms.FileInput(attrs=form_file), label='Imagen', required=False)

    class Meta:
        model = User
        fields = ['id', 'categoria', 'nombre','descripcion', 'precio', 'descuento_subscriptor', 'descuento_oferta', 'imagen']
    
class MantenedorUsuario(UserCreationForm):

    roles_choices = [
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador'),
    ]
    id = forms.IntegerField(widget=forms.NumberInput(attrs=form_control), label="ID(Poblar solamente si se desea eliminar)", required=False, )
    rut = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Rut", max_length=15, required=False)
    rol = forms.ChoiceField(choices=roles_choices, widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), label='Tipo de usuario', required=False)
    username = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Username", required=False)
    nombre = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Nombre", required=False)
    apellido = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Apellido", required=False)
    correo = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Correo", required=False)
    direccion = forms.CharField(widget=forms.TextInput(attrs=form_control), label="Dirección", required=False)
    subscrito = forms.BooleanField(widget=forms.CheckboxInput(attrs=form_check), label='Subscripción', required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), label="Contraseña", required=False)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=form_control), label="Confirmar contraseña", required=False)
    imagen = forms.CharField(widget=forms.FileInput(attrs=form_file), label='Imagen', required=False)

    class Meta:
        model = User
        fields = ['id', 'rut', 'rol', 'username', 'nombre','apellido', 'correo', 'direccion', 'subscrito', 'password1', 'password2', 'imagen']


class BodegaForm(forms.Form):

    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.Select(attrs=form_select),
        label='Categoría'
    )
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.none(), 
        widget=forms.Select(attrs=form_select),
        label='Producto'
    )
    cantidad = forms.IntegerField(
        widget=forms.NumberInput(attrs=form_control),
        label='Cantidad'
    )

    class Meta:
        fields = '__all__'

class HoraForm(Form):
    
    previsiones = [
        ('---', '---'),
        ('fonasa', 'Fondo Nacional de Salud (FONASA)'),
        ('isapre_codelco', 'Isapre de Codelco'),
        ('isapre_banmedica', 'Isapre Banmédica'),
        ('isapre_colmena', 'Isapre Colmena'),
        ('isapre_consalud', 'Isapre Consalud'),
        ('isapre_cruzBlanca', 'Isapre Cruz Blanca'),
        ('isapre_cruzNorte', 'Isapre Cruz del Norte'),
        ('isapre_fundacionBancoEstado', 'Isapre Fundación Banco Estado'),
        ('isapre_nuevaMasvida', 'Isapre Nueva Másvida'),
        ('isapre_vidaTres', 'Isapre Vida Tres'),
        ('particular', 'Particular'),
    ]

    especialidades = [
        ('---', '---'),
        ('pediatria', 'Pediatría'),
        ('traumatologia', 'Traumatología'),
        ('cardiologia', 'Cardiología'),
        ('dermatologia', 'Dermatología'),
        ('endocrinologia', 'Endocrinología'),
        ('fonoaudiologia', 'Fonoaudiología'),
        ('geriatria', 'Gertiatría'),
        ('ginecologia', 'Ginecología'),
        ('urologia', 'Urología'),
        ('kinesiologia', 'Kinesiología'),
        ('Oncología', 'Oncología'),
    ]

    doctores = [
        ('---', '---'),
        ('camiloGonzalez', 'Camilo González'),
        ('jorgePerez', 'Jorge Pérez'),
        ('piaArroyo', 'Pía Arroyo'),
    ]

    rut = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'Ej: 19.283.294-1'}), label="Rut", required=True)
    prevision = forms.ChoiceField(choices=previsiones, widget=forms.Select(attrs={'class': 'form-control'}), label="Previsión de Salud", required=True)
    especialidad = forms.ChoiceField(choices=especialidades, widget=forms.Select(attrs={'class': 'form-control'}), label="Especialidad", required=True)
    doctor = forms.ChoiceField(choices=doctores, widget=forms.Select(attrs={'class': 'form-control'}), label="Doctor/a", required=True)
    fecha = forms.DateField(widget=SelectDateWidget(attrs={'class': 'form-control'}))
    class Meta:
        fields = ['rut', 'prevision', 'especialidad', 'doctor']