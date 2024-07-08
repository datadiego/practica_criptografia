from Crypto.Cipher import ChaCha20
from base64 import b64decode, b64encode
from Crypto.Cipher import ChaCha20_Poly1305
from Crypto.Random import get_random_bytes

# Datos
mensaje = 'KeepCoding te enseña a codificar y a cifrar'
clave = 'AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120'
nonce = get_random_bytes(12) # No se debe fijar, siempre debe ser unico
datos_asociados = 'Datos no cifrados sólo autenticados'

print('Mensaje:', mensaje)
print('Clave:', clave)
print('Nonce:', nonce)
print('Datos asociados:', datos_asociados)
print("--------")

# Conversiones

mensaje_bytes = bytes(mensaje, 'UTF-8')
clave_bytes = bytes.fromhex(clave)
nonce_bytes = nonce
datos_asociados_bytes = bytes(datos_asociados, 'UTF-8')

cipher = ChaCha20_Poly1305.new(key=clave_bytes, nonce=nonce_bytes)
cipher.update(datos_asociados_bytes)
texto_cifrado = cipher.encrypt(mensaje_bytes)
print('Mensaje cifrado: ', texto_cifrado.hex())
print('Clave:', clave)
print('Nonce:', nonce)
print('Datos asociados:', datos_asociados)
print("--------")
