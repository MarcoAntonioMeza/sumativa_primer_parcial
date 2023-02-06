from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin)

# Create your models here.

status_user =[
    (True, 'Si'),
    (False,'No')
]

class ManejadorUsuario(BaseUserManager):

    def create_user(self, correo, password ,nombre, apellidos,**otros):
        if not correo:
            raise ValueError(('Los usuarios deben tener un correo válido'))

        email = self.normalize_email(correo)
        usuario = self.model(
                email = email,
                nombre = nombre,
                apellidos = apellidos,
                **otros
        )

        usuario.set_password(password)

        usuario.save(using=self._db)

        return usuario

    #Crea y guarda  super-usuario 
    def create_superuser(self, correo, password,nombre, apellidos,**otros):
        otros.setdefault('is_staff', True)
        otros.setdefault('is_superuser', True)
        otros.setdefault('is_active', True)

        usuario =  self.create_user(
            email= correo,
            password=password,
            nombre = nombre,
            apellidos = apellidos,
            **otros
        )
        usuario.save(using=self._db)
        return usuario
    '''
    #Crea y guarda  usuario staff
    def create_staffuser(self, correo, password):
        usuario = self.create_user(
            correo,
            password = password,
        )
        usuario.is_staff = True
        usuario.save(using=self._db)
        return usuario
    '''
        

        

class Usuario(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name= 'correo electrónico', unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    """        null = False,
        blank=False,
        choices= status_user,
        default=0
"""
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(('Activo'),default=True)
    

    objects = ManejadorUsuario()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre','apellidos']

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'

    class Meta:
        verbose_name = ('usuario')
        verbose_name_plural = ('usuarios')

    