from django.urls import path
from . import views


urlpatterns = [
    #Url para  el inicio de la aplicacion inicio
    #path('', views.login_usuario, name='login'),
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('buzon/', views.buzon, name='buzon'),
    path('iniciar-sesion/', views.login_usurio, name='login_usuario'),
    path('registrar/', views.registar_usuario, name='registar_usuario'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('home/', views.home, name='home'),
    path('usuarios/', views.usuarios, name='usuarios'),
]