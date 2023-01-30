from .forms import *


def login_form(request):
    login_form = LoginUsuario()
    
    return {
        'loginForm': login_form,
    }