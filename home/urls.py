from django.urls import path
from . import views


urlpatterns = [
    #Url para  el inicio de la aplicacion inicio
    #path('', views.login_usuario, name='login'),
    path('', views.login_usurio, name='login_usuario'),
    path('registrar', views.registar_usuario, name='registar_usuario'),
]