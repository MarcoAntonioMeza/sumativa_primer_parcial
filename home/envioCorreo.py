from django.conf import settings
from django.core.mail import EmailMultiAlternatives
import pywhatkit 

def send_user_mail(correo,code):
    subject = 'Código de verificación'

    
    message = EmailMultiAlternatives(subject , #Titulo,
                                    settings.EMAIL_HOST_USER, #Remitente
                                    [correo]) #Destinatario
    
    message.attach_alternative(f'Su código es: {code}', 'text/html')
    message.send()


def msg_what(code):
    # importamos el modulo
    # utilizaremos controles de excepciones
    try: 
        
    # enviando mensaje al receptor
    # usando pywhatkit 
        pywhatkit.sendwhatmsg("+522481950132",  
                            code,  
                            22, 28) 
        print("Envio Exitoso!") 
    
    except: 
        
    # manejo de excepcion
    # e impresion del error
        print("Ha ocurrido un error!")