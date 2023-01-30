from django.urls import path
from . import views


urlpatterns = [
    #Url para  el inicio de la aplicacion inicio
    path('', views.index, name='index'),
]