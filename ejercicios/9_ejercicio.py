import hashlib
import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Datos
clave="A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72"
mensaje="00000000000000000000000000000000"
iv="00000000000000000000000000000000"
print('Clave:', clave)
print('Mensaje:', mensaje)
print('IV:', iv)
print("--------")
# Cifrado
mensaje_bytes = bytes.fromhex(mensaje)
clave_bytes = bytes.fromhex(clave)
iv_bytes = bytes.fromhex(iv)
cipher = AES.new(clave_bytes, AES.MODE_CBC,iv_bytes)
texto_cifrado_bytes = cipher.encrypt(pad(mensaje_bytes, AES.block_size,  style='pkcs7'))

# KCV AES
print("KCV AES:", texto_cifrado_bytes.hex()[0:6])
print("--------")
# KCV SHA256
m = hashlib.sha256()
m.update(bytes.fromhex("A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72"))
print("KCV SHA256: " + m.digest().hex()[0:6])