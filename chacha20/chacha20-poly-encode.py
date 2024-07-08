from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json

try:
    mensaje = 'KeepCoding es una gran oportunidad de aprender muchas cosas sobre ciberseguridad'
    clave = 'c936108299307d3f6f7585b96013346d043f3920b03284c6b45253fd51a545ca' #256 o 128 bits de clave, 64 caracteres hexadecimales
    nonce = get_random_bytes(12) # No se debe fijar, siempre debe ser unico
    datos_asociados = 'Datos no cifrados sólo autenticados' # Datos no cifrados, solo autenticados
    print('Mensaje:', mensaje)
    print('Clave:', clave)
    print('Nonce:', nonce)
    print('Datos asociados:', datos_asociados)
    print("--------")
    # Conversiones
    mensaje_bytes = bytes(mensaje, 'UTF-8')
    clave_bytes = bytes.fromhex(clave)
    datos_asociados_bytes = bytes(datos_asociados, 'UTF-8')

    cipher = ChaCha20_Poly1305.new(key=clave_bytes, nonce=nonce) # Se cifra con la clave y el nonce
    cipher.update(datos_asociados_bytes) # Se actualiza el cifrado con los datos asociados
    texto_cifrado, tag = cipher.encrypt_and_digest(mensaje_bytes)

    #Simulamos el mensaje que se debe enviar, en este caso lo enviaremos todo el contenido en base64
    mensaje_enviado = { "nonce": b64encode(nonce).decode(),"datos asociados": b64encode(datos_asociados_bytes).decode(), "texto cifrado": b64encode(texto_cifrado).decode(), "tag": b64encode(tag).decode()}
    json_mensaje = json.dumps(mensaje_enviado)
    #print("Mensaje: ", json_mensaje)
    print("Nonce:", mensaje_enviado["nonce"])
    print("Datos asociados:", mensaje_enviado["datos asociados"])
    print("Texto cifrado:", mensaje_enviado["texto cifrado"])
    print("Tag:", mensaje_enviado["tag"])
    print("--------")


except (ValueError, KeyError) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error)