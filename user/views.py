from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import LoginUsuario

# Create your views here.

def login_usuario(request):
    login_form = LoginUsuario(request.POST or None)
    if login_form.is_valid():
        correo = login_form.cleaned_data.get('correo')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, correo=correo, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesion correctamente')
            return render(request,'inicio/index.html')
        else:
            messages.warning(
                request, 'Correo Electronico o Contrasena invalida')
            return redirect('login')

    messages.error(request, 'Formulario Invalido')
    #return redirect('network:home')
    return render(request,'inicio/login.html')

def registar_usuario(request):
    return render(request,'inicio/index.html')

