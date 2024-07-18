import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Datos de entrada
textoPlano_bytes = bytes('KeepCoding mola un montón.', 'UTF-8')
clave = get_random_bytes(16)
#clave = bytes.fromhex('c936108299307d3f6f7585b96013346d')
iv_bytes = bytes.fromhex('47e6831df094b7a6c0ef1fbe0da96ad3')

# Crear cipher
cipher = AES.new(clave, AES.MODE_CBC,iv_bytes)

# Cifrar
texto_cifrado_bytes = cipher.encrypt(pad(textoPlano_bytes, AES.block_size,  style='pkcs7'))

iv_b64 = b64encode(cipher.iv).decode('utf-8') # si generamos el iv de forma aleatoria se puede recuperar asi

texto_cifrado_b64 = b64encode(texto_cifrado_bytes).decode('utf-8') # convertimos a base64
mensaje_json = json.dumps({'iv':iv_b64, 'texto cifrado':texto_cifrado_b64}) # creamos un json con los datos cifrados y el iv
print(mensaje_json)
