from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from user.forms import *
from user.models import Usuario

# Create your views here.


def login_usurio(request):
    if request.POST:
        login_form = LoginUsuario(request.POST or None)
        if login_form.is_valid():
            correo = login_form.cleaned_data.get('correo')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, correo=correo, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'usuarios/login.html')

        # messages.error(request, 'Formulario Invalido')
    return render(request, 'usuarios/login.html')


def registar_usuario(request):
    if request.POST:
        signup_form = RegistrarUsuario(request.POST or None)
        if signup_form.is_valid():
            correo = signup_form.cleaned_data.get('correo')
            nombre = signup_form.cleaned_data.get('nombre')
            apellidos = signup_form.cleaned_data.get('apellidos')
            password = signup_form.cleaned_data.get('password')
            try:
                user = get_user_model().objects.create(
                    correo=correo,
                    nombre=nombre,
                    apellidos=apellidos,
                    password=make_password(password),
                    is_active=True
                )
                login(request, user)
                return redirect('home')

            except Exception as e:
                print(e)
                return JsonResponse({'detail': f'{e}'})
    return render(request,'usuarios/registrar.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login_usuario')

def home(request):
    return render(request,'home/home.html')

def index(request):
    return render(request,'home/index.html')

def contacto(request):
    return render(request,'home/contacto.html')

def ayuda(request):
    return render(request,'home/ayuda.html')

def buzon(request):
    return render(request,'home/buzon.html')

@login_required
def usuarios(request):
    usuarios = Usuario.objects.all()
    #usuarios = list(Usuario.objects.values())
    #return JsonResponse(usuarios)
    return render(request,'usuarios/usuarios.html',{
        'usuarios':usuarios
    })