from .forms import *


def login_form(request):
    login_form = LoginUsuario()
    signupForm = RegistrarUsuario()
    registrar = RegistrarUsuarioAdmin()
    
    return {
        'loginForm': login_form,
        'signupForm': signupForm,
        'registrar': registrar,
    }