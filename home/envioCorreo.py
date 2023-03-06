from django.conf import settings
from django.core.mail import EmailMultiAlternatives

def send_user_mail(correo,code):
    subject = 'Código de verificación'

    
    message = EmailMultiAlternatives(subject , #Titulo,
                                    settings.EMAIL_HOST_USER, #Remitente
                                    [correo]) #Destinatario
    
    message.attach_alternative(f'Su código es: {code}', 'text/html')
    message.send()