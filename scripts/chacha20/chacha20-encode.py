from Crypto.Cipher import ChaCha20
from base64 import b64decode, b64encode

mensaje = 'Si has llegado hasta aquí tienes posibilidades de ser un fuera de serie'
#Se requiere o 256 o 128 bits de clave, por ello usamos 256 bits que se transforman en 64 caracteres hexadecimales
clave = 'c936108299307d3f6f7585b96013346d043f3920b03284c6b45253fd51a545ca' # debe ser de 256 bits o 128 bits
nonce = 'fbdbffb77f5966b2' # deberia ser aleatorio
print('Mensaje:', mensaje)
print('Clave:', clave)
print('Nonce:', nonce)

mensaje_bytes = bytes(mensaje, 'UTF-8')
clave_bytes = bytes.fromhex(clave)
nonce_bytes = bytes.fromhex(nonce)
#Con la clave y con el nonce se cifra. El nonce debe ser único por mensaje
cipher = ChaCha20.new(key=clave_bytes, nonce=nonce_bytes)
texto_cifrado = cipher.encrypt(mensaje_bytes)

print('Mensaje cifrado: ', texto_cifrado.hex())