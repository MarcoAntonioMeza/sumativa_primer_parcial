from django.urls import path
from . import views
from django.conf.urls import handler404
from django.contrib.auth import views as auth_views


handler404 = views.pag_404_not_found

urlpatterns = [
    #Url para  el inicio de la aplicacion inicio
    #path('', views.login_usuario, name='login'),
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('buzon/', views.buzon, name='buzon'),
    path('iniciar-sesion/', views.login_usurio, name='login_usuario'),
    path('registrar/', views.registar_usuario, name='registar_usuario'),
    path('registrar-usuario/', views.registar_usuarios, name='registrar_usuarios'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('home/', views.home, name='home'),
    path('usuarios/', views.usuarios, name='usuarios'),

    path('buscar/', views.buscar, name='buscar'),

    path('validar/', views.validar_codigo, name='codigo'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="autenticacion/password-reset.html"), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(template_name="autenticacion/mensaje.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="autenticacion/password-confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    

]