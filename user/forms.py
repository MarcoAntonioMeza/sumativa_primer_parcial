from  django import forms
from .models import Usuario

class LoginUsuario(forms.Form):
    class Meta():
        model = Usuario
        fields = ['correo','password']

    correo = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'id': 'loginEmail',
                'type': 'email',
                'class': 'form-control'
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'loginPassword',
            'type': 'password',
            'class': 'form-control',
            })
    )