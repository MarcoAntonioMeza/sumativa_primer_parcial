from .forms import *


def login_form(request):
    login_form = LoginUsuario()
    signupForm = RegistrarUsuario()
    
    return {
        'loginForm': login_form,
        'signupForm': signupForm
    }