import jks
import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Obteniendo el path
path = os.path.dirname(__file__)
keystore = path + "/KeyStorePracticas"

ks = jks.KeyStore.load(keystore, "123456")
clave=""
for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-aes-256":
        clave = sk.key.hex()
mensaje_cifrado="TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI="
iv = "00000000000000000000000000000000"
print("-----")
print("Clave: ", clave)
print("Mensaje cifrado: ", mensaje_cifrado) #base64
print("IV: ", iv)
print("-----")
# Desciframos el mensaje

# Descifrado
try:
    mensaje_cifrado_bytes = base64.b64decode(mensaje_cifrado)
    iv_bytes = bytes.fromhex(iv)
    clave_bytes = bytes.fromhex(clave)
    cipher = AES.new(clave_bytes, AES.MODE_CBC, iv_bytes)
    cipher_x923 = AES.new(clave_bytes, AES.MODE_CBC, iv_bytes)
    mensaje_des_bytes = unpad(cipher.decrypt(mensaje_cifrado_bytes), AES.block_size, style="x923")
    mensaje_des_bytes_x923 = unpad(cipher_x923.decrypt(mensaje_cifrado_bytes), AES.block_size, style="x923")
    print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))
    print("Usando x923: ", mensaje_des_bytes_x923.decode("utf-8"))

except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 


