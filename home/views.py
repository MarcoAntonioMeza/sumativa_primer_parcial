from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.defaults import page_not_found
from user.forms import *
from user.models import Usuario, Auth2AF
from . import codigo as totp
from . import envioCorreo as envio

# Create your views here.


def login_usurio(request):
    if request.POST:
        login_form = LoginUsuario(request.POST or None)
        if login_form.is_valid():
            correo = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')

            user = authenticate(request, email=correo, password=password)

            if user is not None:
                key = totp.generar_key()
                codigo = totp.generar_codigo(key)
                a = envio.send_user_mail(correo,codigo)
                envio.msg_what(codigo)
                print(a)

                #user = Usuario.objects.get(email=correo)
                user.auth2af_set.create(key = key, code= codigo)

                return render(request,'usuarios/verificacion.html', {
                    'correo' : correo,
                    'dino_se' : password,
                    'error' : False
                })
            else:
                return render(request, 'usuarios/login.html')
    return render(request, 'usuarios/login.html')

def validar_codigo(request):
    if request.POST:
        code = request.POST['code']
        email = request.POST['correo']
        password = request.POST['dino']

        usuario = Usuario.objects.get(email=email)
        #usuario.auth2af_set.all().delete()
        
        info_user = usuario.auth2af_set.get()

        if code == info_user.code:
            user = authenticate(request, email=email, password=password)
            login(request, user)
            usuario.auth2af_set.all().delete()
            return redirect('home')
        else: 
            return render(request,'usuarios/verificacion.html', {
                    'correo' : email,
                    'dino_se' : password,
                    'error' : 'El código es incorrecto'
                })
    


def registar_usuarios(request):
    if request.POST:
        print(request.POST)
        signup_form = RegistrarUsuario(request.POST or None)
        if signup_form.is_valid():
            correo = signup_form.cleaned_data.get('email')
            nombre = signup_form.cleaned_data.get('nombre')
            apellidos = signup_form.cleaned_data.get('apellidos')
            password = signup_form.cleaned_data.get('password')
            try:
                user = get_user_model().objects.create(
                    email=correo,
                    nombre=nombre,
                    apellidos=apellidos,
                    password=make_password(password),
                    is_active=True
                )
                #login(request, user)
                return redirect('usuarios')

            except Exception as e:
                print(e)
                return JsonResponse({'detail': f'{e}'})
    return render(request, 'usuarios/registrar-usuario.html')


def registar_usuario(request):
    if request.POST:
        print(request.POST)
        signup_form = RegistrarUsuario(request.POST or None)
        if signup_form.is_valid():
            correo = signup_form.cleaned_data.get('email')
            nombre = signup_form.cleaned_data.get('nombre')
            apellidos = signup_form.cleaned_data.get('apellidos')
            password = signup_form.cleaned_data.get('password')
            try:
                user = get_user_model().objects.create(
                    email=correo,
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
    return render(request, 'usuarios/registrar.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('login_usuario')


@login_required(login_url='login_usuario')
def home(request):
    return render(request, 'home/home.html')


def index(request):
    return render(request, 'home/index.html')


def contacto(request):
    return render(request, 'home/contacto.html')


def ayuda(request):
    return render(request, 'home/ayuda.html')


@login_required(login_url='login_usuario')
def buzon(request):
    return render(request, 'home/buzon.html')


@login_required(login_url='login_usuario')
def usuarios(request):
    usuarios = Usuario.objects.all()
    # usuarios = list(Usuario.objects.values())
    # return JsonResponse(usuarios)
    return render(request, 'usuarios/usuarios.html', {
        'usuarios': usuarios
    })


def buscar(request):
    if request.method == "GET":
        usuarios = list(Usuario.objects.filter( nombre__contains=request.GET['nombre']).values())
        return JsonResponse(usuarios, safe=False)
    else:
        return HttpResponse("Solo Ajax")
    


def pag_404_not_found(request, exception, template_name="error/404.html"):
    response = render("404.html")
    response.status_code=404
    return response