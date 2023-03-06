import pyotp

def generar_key():
    return  pyotp.random_base32()

def generar_codigo(key):
    totp = pyotp.TOTP(key)
    codigo = totp.now()
    return codigo

def verificar_codigo(key,codigo):
    totp = pyotp.TOTP(key)
    return totp.verify(codigo)

