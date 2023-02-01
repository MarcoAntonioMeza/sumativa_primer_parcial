from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from user.forms import LoginUsuario

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
                return render(request,'home/home.html')
            else:
                return render(request,'usuarios/login.html',{'error ': "Correo  o Contrasena incorrecta"})

        #messages.error(request, 'Formulario Invalido')
    return render(request,'usuarios/login.html')

def registar_usuario(request):
    return render(request,'usuarios/registrar.html')